from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from localingredients.config import Config
from collections import defaultdict
import os
basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    from localingredients.users.routes import users
    from localingredients.recipes.routes import recipes
    from localingredients.main.routes import main
    from localingredients.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(recipes)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app
