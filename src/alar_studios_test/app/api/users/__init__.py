from flask import Blueprint, jsonify, g, request

from alar_studios_test.app.api.auth import auth_required
from alar_studios_test.db.connection import db_session
from alar_studios_test.db.models import User

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/', methods=['GET'])
@auth_required
def get_all():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


@bp.route('/<int:user_id>', methods=['GET'])
@auth_required
def get(user_id: int):
    user: User = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return jsonify({'error': True, 'message': 'User not found'}), 404
    return jsonify(user.to_dict())


# @bp.route('/', methods=['POST'])
# @auth_required
# def create():
#     user, error = create_user()
#     if error is not None:
#         return jsonify({'error': True, 'message': error}), 400
#     return jsonify(user.to_dict()), 201


@bp.route('/<int:user_id>', methods=['PUT'])
@auth_required
def update(user_id: int):
    user: User = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return jsonify({'error': True, 'message': 'User not found'}), 404
    current_user: User = g.user
    if not current_user.permissions.update:
        return jsonify({'error': True, 'message': 'You have no permissions for operation'}), 401
    # TODO: Add validation
    if data := request.json.get('name'):
        user.name = data
    for permission in ['create', 'update', 'delete']:
        data = request.json.get(permission)
        if data is None:
            continue
        if not getattr(current_user.permissions, permission):
            return jsonify({'error': True, 'message': 'You have no permissions for operation'})
        setattr(user.permissions, permission, data)
    db_session.commit()
    return jsonify(user.to_dict()), 202


@bp.route('/<int:id>', methods=['DELETE'])
@auth_required
def delete(id):
    pass  # 204
