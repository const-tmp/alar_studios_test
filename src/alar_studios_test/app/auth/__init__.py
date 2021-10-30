import functools

from flask import Blueprint, redirect, url_for, session, request, flash, render_template, g
from werkzeug.security import check_password_hash

from alar_studios_test.db.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_url_path='/assets')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    if request.path.startswith('/assets'):
        return None
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        user: User = User.query.filter_by(id=user_id).one_or_none()
        g.user = user
        return


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user: User = User.query.filter_by(name=username).one_or_none()

        if user is None:
            error = 'Incorrect credentials.'
        elif not check_password_hash(user.password_hash, password):
            error = 'Incorrect credentials.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            user.create_token()
            return redirect(url_for('users.index'))

        flash(error, category='danger')

    return render_template('login.html')


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    user: User = User.query.filter_by(name=session['user_id']).one_or_none()
    user.remove_token()
    session.clear()
    return redirect(url_for('index'))
