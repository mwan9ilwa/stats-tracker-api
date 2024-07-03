from flask import Blueprint, jsonify, request
from app.services.github_service import get_user_profile

bp = Blueprint('user', __name__, url_prefix='/api/user')

@bp.route('/profile')
def profile():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    
    user_data = get_user_profile(token)
    return jsonify(user_data)