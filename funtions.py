import json
import sqlite3

con = sqlite3.connect('netflix.db')


def get_title(title):
    """Поиск по названию"""
    cur = con.cursor()
    sqlite_query = "SELECT title, country, release_year, listed_in, description  " \
                   "FROM netflix " \
                   f"WHERE title = '{title}' " \
                   "ORDER BY release_year " \
                   "LIMIT 1"

    cur.execute(sqlite_query)
    for row in cur.fetchone():
        row = dict(title=row[0], country=row[1], release_year=row[2], genre=row[3], description=row[4])
    return row


def get_year_diapason(year_1, year_2):
    """Поиск по диапазону лет выпуска"""
    cur = con.cursor()
    sqlite_query = "SELECT title, release_year  " \
                   "FROM netflix " \
                   f"WHERE release_year BETWEEN '{year_1}' AND '{year_2}' " \
                   "ORDER BY release_year " \
                   "LIMIT 100"

    movie_list = []
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        row = dict(title=row[0], release_year=row[1])
        movie_list.append(row)
    return movie_list


def get_rating(rating_type):
    """Поиск по рейтингу"""
    cur = con.cursor()
    sqlite_query = "SELECT title, rating, description  " \
                   "FROM netflix " \
                   f"WHERE rating IN '{rating_type}' "

    children_list = []
    family_list = []
    adult_list = []

    cur.execute(sqlite_query)
    for row in cur.fetchall():
       row = dict(title=row[0], description=row[1])
       family_list.append(row)
    return family_list


def get_genre(genre):
    """Получает название жанра в качестве аргумента и возвращает 10 самых свежих фильмов в формате json"""
    cur = con.cursor()
    sqlite_query = "SELECT title, genre, description  " \
                   "FROM netflix " \
                   f"WHERE listed_in LIKE '%{genre}%' " \
                   "ORDER BY release_year " \
                   "LIMIT 10"

    cur.execute(sqlite_query)
    for row in cur.fetchall():
        row = dict(title=row[0], description=row[1])
    return row



def get_actors(actor_1, actor_2):
    """ Получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки
    cast и возвращает список тех, кто играет с ними в паре больше 2 раз"""
    cur = con.cursor()
    sqlite_query = "SELECT title, country, release_year, listed_in, description  " \
                   "FROM netflix " \
                   f"WHERE cast LIKE '{actor_1}' " \
                   f"AND cast LIKE '{actor_2}' "

    actors_list = []
    cur.execute(sqlite_query)
    for row in cur.fetchone():
        row = dict(title=row[0], country=row[1], release_year=row[2], genre=row[3], description=row[4])
        actors_list.append(row)
        actors_list = row[0].split(", ")
        actors_list_unique = set(actors_list)

        actors_list_unique.remove(actor_1)
        actors_list_unique.remove(actor_2)
    return actors_list


def get_type_movie(movie_type, year, movie_genre):
    """Передавается тип картины (фильм или сериал), год выпуска и ее жанр"""
    cur = con.cursor()
    sqlite_query = "SELECT type, release_year, listed_in, description " \
                   "FROM netflix " \
                   f"WHERE type = '{movie_type}' " \
                   f"AND release_year = '{year}' " \
                   f"AND listed_in LIKE %{movie_genre}% "

    cur.execute(sqlite_query)
    for row in cur.fetchone():
        row = dict(title=row[0], release_year=row[1], listed_in=row[2], description=row[3])
    return row
