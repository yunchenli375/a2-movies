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
