import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET')
    GITHUB_REDIRECT_URI = os.getenv('GITHUB_REDIRECT_URI')