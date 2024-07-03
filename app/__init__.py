from flask import Flask
from flask_cors import CORS
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    
    from app.api import auth, user, repo
    app.register_blueprint(auth.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(repo.bp)
    
    @app.route('/health')
    def health_check():
        return 'OK', 200
    
    return app