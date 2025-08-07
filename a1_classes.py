"""A movie list console program tracking movies to watch and watched"""

from movie import Movie
from moviecollection import MovieCollection

__author__ = "Yunchen Li"

JSON_FILE = "movies.json"
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
MENU = "Menu:\nD - Display movies\nA - Add new movie\nW - Watch a movie\nQ- Quit"
MENU_CHOICES = "dawq"

