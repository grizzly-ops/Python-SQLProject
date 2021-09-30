import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
	id INTERGER PRIMARY KEY,
	title TEXT,
	release_timestamp REAL,
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTE watched (
	username TEXT PRIMARY KEY
);"""

CREATE_WATCHLIED_TABLE = """
	user_username TEXT,
	movie_id INTEGER,
	FORIGEN KEY(user_username) REFERENCES user(username),
	FORIGEN KEY(movie_id) REFERENCES movies(id)
);"""


INSERT_MOVIES = "INSERT INTO movies(title, release_timestamp,) VALUES (?, ?);"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
DELETE_MOVIE = "SELECT FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = """SELECT movies.* FROM movies 
JOIN watched ON movies_id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE user_username = ?;"""
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SET_MOVIE_WATHCED = "UPDATE movies SET watched = 1 WHERE title = ?;"
SEARCH_MOVIES = "SELECT * FROM movies where title LIKE ?;"


connection = sqlite3.connect("data.db")


def create_tables():
	with connection:
		connection.execute(CREATE_MOVIES_TABLE)
		connection.execute(CREATE_USERS_TABLE)
		connection.execute(CREATE_WATCHLIST_TABLE)


def add_user(username):
	with connection:
		connection.excute(INSERT_USER,(username,))

def add_movie(title, release_timestamp):
	with connection:
		connection.execute(INSERT_MOVIES,(title, release_timestamp))


def get_movies(upcoming=False):
	with connection:
		cursor = connection.cursor()
		if upcoming:
			today_timestamp = datetime.datetime.today().timestamp()
			cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
		else:	
			cursor.execute(SELECT_ALL_MOVIES)
		return cursor.fetchall()


def watch_movie(username, movie_id):
	with connection:
		connection.execute(INSERT_WATCHED_MOVIE,(username, movie_id ))


def get_watched_movies(username):
	with connection:
		cursor = connection.cursor
		cursor.execute(SELECT_WATCHED_MOVIES,(username,))
		return cursor.fetchall()















