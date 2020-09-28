from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "auth.login"
bootstrap = Bootstrap()


def create_app(config="DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(f"project.config.{config}")

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login.init_app(app)
    bootstrap.init_app(app)

    from project.errors.handlers import bp as errors_bp
    app.register_blueprint(errors_bp)

    from project.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from project.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
