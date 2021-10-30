import secrets

from flask import Flask, url_for, g
from werkzeug.utils import redirect

from alar_studios_test.app.api import bp as api_bp
from alar_studios_test.app.api.auth import enable_token_auth
from alar_studios_test.app.auth import bp as auth_bp, login_required
from alar_studios_test.app.cors import enable_cors
from alar_studios_test.app.json import bp as json_bp
from alar_studios_test.app.users import bp as users_bp
from alar_studios_test.config import APP_DIR
from alar_studios_test.db.connection import db_session


def create_app() -> Flask:
    app = Flask(
        __name__,
        static_url_path='/assets',
        static_folder=str(APP_DIR / 'assets'),
        template_folder=str(APP_DIR / 'assets/html/templates')
    )

    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex()
    )

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(json_bp)

    # enable_token_auth(app)    # dummy token auth
    # enable_cors(app)          # dummy CORS support

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        if exception is not None:
            app.logger.exception(exception)
        db_session.remove()

    @app.context_processor
    def user_context():
        return dict(current_user=g.user)

    @app.route('/')
    @login_required
    def index():
        return redirect(url_for('users.index'))

    return app


if __name__ == '__main__':
    create_app()
