from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application

def register_extensions(app: Flask):
    db.init_app(app)
    db.create_all()
    api = Api(app)

    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
