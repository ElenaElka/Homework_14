import sqlite3

con = sqlite3.connect('netflix.db', check_same_thread=False)


def get_title(title):
    """Поиск по названию"""
    cur = con.cursor()
    sqlite_query = "SELECT title, country, release_year, listed_in, description  " \
                   "FROM netflix " \
                   f"WHERE title = '{title}' " \
                   "ORDER BY release_year " \
                   "LIMIT 1"

    cur.execute(sqlite_query)
    row = cur.fetchone()
    data = dict(title=row[0], country=row[1], release_year=row[2], genre=row[3], description=row[4])
    return data


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

    rating_type_list = []
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        row = dict(title=row[0], description=row[1])
        rating_type_list.append(row)
    return rating_type_list


def get_genre(genre):
    """Получает название жанра в качестве аргумента и возвращает 10 самых свежих фильмов в формате json"""
    cur = con.cursor()
    sqlite_query = "SELECT title, description  " \
                   "FROM netflix " \
                   f"WHERE listed_in LIKE '%{genre}%' " \
                   "ORDER BY release_year " \
                   "LIMIT 10"

    movie_genre_list = []
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        row = dict(title=row[0], description=row[1])
        movie_genre_list.append(row)
    return movie_genre_list


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
    for row in cur.fetchall():
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
    sqlite_query = "SELECT title, type, release_year, listed_in, description " \
                   "FROM netflix " \
                   f"WHERE type = '{movie_type}' " \
                   f"AND release_year = '{year}' " \
                   f"AND listed_in LIKE '%{movie_genre}%' "

    movie_type_list = []
    cur.execute(sqlite_query)
    for row in cur.fetchall():
        row = dict(title=row[0], type=row[1], release_year=row[2], listed_in=row[3], description=row[4])
        movie_type_list.append(row)
    return movie_type_list
