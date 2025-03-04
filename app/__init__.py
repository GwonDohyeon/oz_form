from config import db
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from routes import *

migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)
    
    api=Api(application)
    api.register_blueprint(index_blp)
    api.register_blueprint(answer_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(image_blp)
    api.register_blueprint(question_blp)
    api.register_blueprint(choice_blp)

    return application
