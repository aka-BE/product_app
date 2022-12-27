from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session



# Globally accessible library
db = SQLAlchemy()
session = Session()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')


    # Initialize Plugins
    db.init_app(app)
    session.init_app(app)


    with app.app_context():
        # Include our Routes
        from . import routes   # Import routes

        db.create_all()     # Create sql tables for our data models


        return app