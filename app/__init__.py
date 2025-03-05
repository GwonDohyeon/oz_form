from config import db
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from .routes import index_blp,answer_blp,choice_blp,question_blp,image_blp,user_blp

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")
    app.secret_key = "oz_form_secret"

    db.init_app(app)

    migrate.init_app(app, db)
    
    api=Api(app)
    api.register_blueprint(index_blp)
    api.register_blueprint(answer_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(image_blp)
    api.register_blueprint(question_blp)
    api.register_blueprint(choice_blp)

    return app
