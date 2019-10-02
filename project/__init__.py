from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Production config
app.config.from_object("project.config.ProductionConfig")

# Development config
# app.config.from_object("project.config.DevelopmentConfig")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = "login"
bootstrap = Bootstrap(app)

from project import routes, models, errors
