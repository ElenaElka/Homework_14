from flask import Flask, jsonify
from funtions import get_title, get_year_diapason, get_rating, get_genre, get_actors, get_type_movie


app = Flask(__name__)


@app.route('/movies/<title>')
def title_search(title):
    movies = get_title(title)
    return jsonify(movies)


@app.route('/years/<int:year_1>/to/<int:year_2>')
def years_search(year_1, year_2):
    movies_year = get_year_diapason(year_1, year_2)
    return jsonify(movies_year)


@app.route('/movie/rating/<group_type>')
def rating_search(group_type):
    movies_group = get_rating(group_type)

    children_list = []
    family_list = []
    adult_list = []
    movie_dict = children_list + family_list + adult_list

    for movie in movies_group:
        if movie == 'children':
           children_list.append(movie)
        if movie == 'family':
           family_list.append(movie)
        else:
           adult_list.append(movie)

    return jsonify(movie_dict)


@app.route('/movie/<genre>')
def genre_search(genre):
    movies_genre = get_genre(genre)
    return jsonify(movies_genre)

@app.route('/movie/<actor>')
def actors_search(actor):
    movies_actors = get_actors(actor)
    return jsonify(movies_actors)

@app.route('/movie/<type>/<int:year_release>/<genre>')
def type_movie_search(type, year_release, genre):
    movies_type = get_type_movie(type, year_release, genre)
    return jsonify(movies_type)

app.run()