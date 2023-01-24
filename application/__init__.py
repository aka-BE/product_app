from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session



# Globally accessible library
db = SQLAlchemy()
login_manager = LoginManager()
session = Session()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Application Configuration
    app.config.from_object('config.Config')


    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    session.init_app(app)


    with app.app_context():
        # Import parts of our application
        from . import routes, auth

        # Register Blueprints
        app.register_blueprint(routes.home_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()


        return app
