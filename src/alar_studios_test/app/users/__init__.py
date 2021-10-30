from flask import Blueprint, render_template, request, g, flash, url_for
from sqlalchemy.exc import DatabaseError
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from alar_studios_test.app.auth import login_required
from alar_studios_test.db.connection import db_session
from alar_studios_test.db.models import User, Permissions

bp = Blueprint('users', __name__, url_prefix='/users', template_folder='templates')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        error = None
        username = request.form.get('name')
        password = request.form.get('password')
        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        form_permissions = request.form.getlist('permissions')
        current_user: User = g.user
        new_user = User(name=username, password_hash=generate_password_hash(password))
        permissions = Permissions(user=new_user)
        # TODO: Add validation
        # user can't set more permissions, than he has
        if current_user.permissions.create and 'create' in form_permissions:
            permissions.create = True
        if current_user.permissions.update and 'update' in form_permissions:
            permissions.update = True
        if current_user.permissions.delete and 'delete' in form_permissions:
            permissions.delete = True
        db_session.add(permissions)
        try:
            db_session.commit()
        except DatabaseError:
            db_session.rollback()
            error = f"User {username} is already registered."

        if error is not None:
            flash(error, category='danger')

    users = User.query.all()
    return render_template('users.html', users=users)


@bp.route('/delete', methods=('POST',))
@login_required
def delete():
    current_user: User = g.user
    error = None
    user_id = request.form.get('user_id')

    if not current_user.permissions.delete:
        error = 'You have no permissions for operation.'

    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        error = 'Invalid user'

    if error is not None:
        flash(error, category='danger')
        return render_template('users.html', users=User.query.all())

    db_session.delete(user)
    db_session.delete(user.permissions)
    db_session.commit()

    return redirect(url_for('.index'))
