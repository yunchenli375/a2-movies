"""A movie list console program tracking movies to watch and watched"""

from movie import Movie
from moviecollection import MovieCollection

__author__ = "Yunchen Li"

JSON_FILE = "movies.json"
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
MENU = "Menu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ- Quit"
MENU_CHOICES = "dawq"


def main():
    """program entrypoint"""
    print(f"Must-See Movies 1.1 - by {__author__}")
    movie_collection = MovieCollection()
    movie_collection.load_movies(JSON_FILE)
    movie_collection.sort("year")
    print(f"{len(movie_collection.movies)} movies loaded from movies.json")

    # According to the CP1404 Assignment 1 specification and sample output from the PDF file,
    # initial display of movie details does not exist.
    # print(movie_collection)

    print(MENU)
    choice = get_non_empty_string(">>> ").lower()[0]
    while choice != "q":
        if choice == "d":
            print(movie_collection)
        elif choice == "a":
            add_movie(movie_collection)
        elif choice == "w":
            watch_movie(movie_collection)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = get_non_empty_string(">>> ").lower()[0]

    movie_collection.save_movies(JSON_FILE)
    print(f"{len(movie_collection.movies)} movies saved to movies.json")
    print("Have a nice day :)")


def add_movie(collection):
    """Get a new movie from the user with validation."""
    title = get_non_empty_string("Title: ")
    year = get_positive_integer("Year: ")
    category = CATEGORIES[get_valid_category(CATEGORIES)]
    new_movie = Movie(title, year, category, False)
    collection.add_movie(new_movie)
    print(
        f"{new_movie.title} ({new_movie.category} from {new_movie.year}) added to movie list."
    )
    collection.sort("year")

