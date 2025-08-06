"""MovieCollection class definition"""

import json
from operator import attrgetter

from movie import Movie


class MovieCollection:
    """Represents a collection of movies, allowing for loading, adding, sorting, and saving movies."""

    YEAR_WIDTH = 4

    def __init__(self):
        """Initializes a empty MovieCollection."""
        self.movies = []

    def get_number_of_watched_movies(self):
        """Returns the number of unwatched movies in the collection."""
        return sum(1 for movie in self.movies if movie.is_watched)

    def get_number_of_unwatched_movies(self):
        """Returns the number of unwatched movies in the collection."""
        return len(self.movies) - self.get_number_of_watched_movies()

    # About load_movies and save_movies:
    # Including creation of file object in read file or write file function breaks the principle of single responsibility,
    # because it mixes file handling with data management.
    # The save/load function should only handle the serialization of movie data with a file-like object, instead of a specific file path.
    # Because of the immutable tests in test_moviecollection.py, these functions have to accept a filename as their parameter.
    def load_movies(self, filename):
        """Loads movies from a JSON file into the collection."""
        with open(filename) as file:
            self.movies = [
                Movie.from_dict(movie_data) for movie_data in json.load(file)
            ]

