import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Setting base dir 
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Setting up the database directory
    db_dir = os.path.join(basedir, '../data')

    # Using Fstring to insert the database directory into the URI. Python has issues with relative pathing. 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(db_dir, 'dev.db')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .models import User, Employee  # Import models here to avoid circular issues

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        try:
            db.create_all()
        except Exception as e:
            print(f"Database creation failed: {e}")
            raise

        if os.getenv("FLASK_ENV") == "development" and os.getenv("FORCE_SEED") == "true":
            from .seed_db import seed_database
            seed_database(db, Employee)

    # Register Blueprints
    from .routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    from .auth_routes import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .user_routes import users as users_blueprint
    app.register_blueprint(users_blueprint)

    from .department_routes import departments as departments_blueprint
    app.register_blueprint(departments_blueprint)

    return app