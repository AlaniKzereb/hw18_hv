from flask import request
from flask_restx import Resource, Namespace

from container import movie_service, movie_dao
from dao.model.movie import MovieSchema, Movie

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies = movie_service.get_all()
        did = request.args.get('director_id')
        if did:
            movies = movie_service.get_by_director(did)
        gid = request.args.get('genre_id')
        if gid:
            movies = movie_service.get_by_genre(gid)
        year = request.args.get('year')
        if year:
            movies = movie_service.get_by_year(year)
        return movies_schema.dump(movies), 200

    def post(self):
        data = request.json
        movie_service.create_movie(data)
        return "Ok", 201

@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update_movie(data)
        return "ok", 201

    def delete(self, mid):
        movie_service.delete_movie(mid)
        return "ok", 201
