"""MovieCollection class definition"""

import json
from operator import attrgetter

from movie import Movie


class MovieCollection:
    """Represents a collection of movies, allowing for loading, adding, sorting, and saving movies."""
