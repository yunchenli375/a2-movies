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


def get_valid_category(categories=CATEGORIES):
    """Returns a valid index of categories from the user."""
    print(f"Categories available: {', '.join(category for category in categories)}")
    choice = get_non_empty_string("Category: ").title()
    try:
        return categories.index(choice)
    except ValueError:
        print(f"Invalid category; using {categories[-1]}")
        return len(categories) - 1


def get_non_empty_string(prompt):
    """Get a non-empty string input from the user."""
    value = input(f"{prompt}")
    while not value:
        print("Input can not be blank")
        value = input(f"{prompt}")
    return value


def watch_movie(collection: MovieCollection):
    """Mark a movie as watched based on user input."""
    if all(movie.is_watched for movie in collection.movies):
        print("No more movies to watch!")
        return
    print("Enter the movie number to mark watched")
    index = get_valid_movie_index(len(collection.movies))
    if collection.movies[index].is_watched:
        print(f"You have already watched {collection.movies[index].title}.")
        return
    collection.movies[index].is_watched = True
    print(
        f"{collection.movies[index].title} ({collection.movies[index].year}) watched."
    )


def get_valid_movie_index(movie_count):
    """Returns a valid movie index(0-based) from the user."""
    choice = get_positive_integer()
    while choice > movie_count:
        print("Invalid movie number")
        choice = get_positive_integer()
    return choice - 1


def get_positive_integer(prompt=">>> "):
    """Get a valid positive integer input from the user."""
    # Reason for not using IndexError and exception pattern:
    # This function can be reused for both year and movie index inputs.
    # Because when displaying the movie list, the index starts from 1, instead of 0.
    # Therefore this function follows the principle of don't repeat yourself.
    # Using IndexError to handle bad movie index input is re-implementing the same logic.
    value = input(f"{prompt}")
    while not value.isdigit() or int(value) < 1:
        try:
            _erroneous_value = int(value)
            print("Number must be >= 1")
        except ValueError:
            # isdigit() returns False for negative numbers
            print("Invalid input; enter a valid number")
        value = input(f"{prompt}")
    return int(value)


