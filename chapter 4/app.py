import datetime
import Database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app
7) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
Database.create_tables

def prompt_add_movie():
    title = input("Movie title:" )
    release_date = input("release date(dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    Database.add_movie(title, timestamp)

def print_movie_list(heading, movies):
    print(f"-- {heading} movies --" )
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{_id}: {title} (on {movie[1]})")
        print("---\n") 
  
def prompt_watch_movie():
    username = input("Username: ")
    movie_id = input("Movie ID")
    database.watch_movie(username, movie_id)

def prompt_show_wached_movies():
    username =input("Username: ")
    movies = Database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched" , movies)
    else:
        print("That user has watched no movies yet!")    

def prompt_add_user():
    username = input("Username: ")
    Database.add_user(username)


while (user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = Database.get_movies(True)
        print_movie_list("Upcomig", movies)
    elif user_input == "3":
        movies = Database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
         prompt_show_watched_movies()
    elif user_input == "6"
        prompt_add_user()
    else:
        print("Invalid input, please try again!")