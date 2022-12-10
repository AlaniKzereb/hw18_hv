from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres), 200

@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
