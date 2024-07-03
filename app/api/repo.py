from flask import Blueprint, jsonify, request
from app.services.github_service import get_user_repos

bp = Blueprint('repo', __name__, url_prefix='/api/repo')

@bp.route('/list')
def list_repos():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'No token provided'}), 401
    
    repos = get_user_repos(token)
    return jsonify(repos)