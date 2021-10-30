from flask import Blueprint

from .users import bp as users_api_bp

bp = Blueprint('api', __name__, url_prefix='/api')
bp.register_blueprint(users_api_bp)
