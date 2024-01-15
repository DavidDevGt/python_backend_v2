from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        from .routes import views
        app.register_blueprint(views)
        
        # Create the tables if not exists
        db.create_all()
    
    return app