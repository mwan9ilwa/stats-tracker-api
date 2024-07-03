import requests
from flask import current_app

def github_login():
    return f'https://github.com/login/oauth/authorize?client_id={current_app.config["GITHUB_CLIENT_ID"]}&redirect_uri={current_app.config["GITHUB_REDIRECT_URI"]}'

def github_callback(code):
    response = requests.post(
        'https://github.com/login/oauth/access_token',
        data={
            'client_id': current_app.config['GITHUB_CLIENT_ID'],
            'client_secret': current_app.config['GITHUB_CLIENT_SECRET'],
            'code': code
        },
        headers={'Accept': 'application/json'}
    )
    return response.json().get('access_token')

def get_user_profile(token):
    response = requests.get(
        'https://api.github.com/user',
        headers={'Authorization': f'token {token}'}
    )
    return response.json()

def get_user_repos(token):
    response = requests.get(
        'https://api.github.com/user/repos',
        headers={'Authorization': f'token {token}'}
    )
    return response.json()