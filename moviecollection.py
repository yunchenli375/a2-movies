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

    def save_movies(self, filename):
        """Saves the movie collection to a JSON file."""
        with open(filename, "w") as file:
            json.dump([vars(movie) for movie in self.movies], file)

    def add_movie(self, movie):
        """Add a Movie instance to the collection."""
        self.movies.append(movie)

    def sort(self, key):
        """Sorts the movies in the collection by a given key, then the title."""
        if key not in Movie.class_data_fields():
            key = "title"
        self.movies.sort(key=attrgetter(key, "title"))

    def __str__(self):
        """Returns a formatted representation of the movie collection.
        This function matches requirements from assignment 1"""
        # Calculate the width information based on the longest title and index in the collection, for pretty printing.
        title_column_width = (
            max(len(movie.title) for movie in self.movies) if self.movies else 0
        )
        index_width = len(str(len(self.movies)))
        # A temporary container to hold the formatted movie details.
        lines = []
        for i, movie in enumerate(self.movies):
            lines.append(
                f"{i + 1:>{index_width}}. {' ' if movie.is_watched else '*'} {movie.title:<{title_column_width}} - {movie.year:>{self.YEAR_WIDTH}} ({movie.category})"
            )
        # The final stastistics line.
        lines.append(
            f"{self.get_number_of_watched_movies()} movies watched. {self.get_number_of_unwatched_movies()} movies still to watch."
        )
        return "\n".join(lines)

