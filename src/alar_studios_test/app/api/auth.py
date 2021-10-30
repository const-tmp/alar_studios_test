import functools

from flask import g, request

from alar_studios_test.db.models import User


def auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return 'Unauthenticated', 401

        return view(**kwargs)

    return wrapped_view


def enable_token_auth(app_or_bp):
    @app_or_bp.before_app_request
    def token_auth():
        if (auth_token := request.headers.get('Authorization')) is not None:
            user = User.check_token(auth_token)
            if user is None:
                g.user = None
            else:
                g.user = user
                user.renew_token()
