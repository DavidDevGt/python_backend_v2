from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(name)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import views
        app.register_blueprint(views)
        
        # Create the tables if not exists
        db.create_all()
    
    return app