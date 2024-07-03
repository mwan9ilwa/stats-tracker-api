from flask import Blueprint, redirect, request, jsonify
from app.services.github_service import github_login, github_callback

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/github')
def login():
    return redirect(github_login())

@bp.route('/callback')
def callback():
    code = request.args.get('code')
    token = github_callback(code)
    # Redirect to the Next.js frontend with the token or a success indicator
    frontend_url = 'http://localhost:3000/dashboard'  # Adjust as necessary
    return redirect(f"{frontend_url}?token={token}")
