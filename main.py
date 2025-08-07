"""
Name: Yunchen Li
Date Started:6/8/20025
Brief Project Description: A Kivy GUI application for managing movie collections.
GitHub URL:https://github.com/cp1404-students/a2-movies-yunchenli375
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection

DATA_FILE_JSON = "movies.json"
PROGRAM_NAME = "Must-See Movies 2.0"
GUI_LAYOUT = "app.kv"
COLOR_UNWATCHED = (1, 0, 0, 1)
COLOR_WATCHED = (0, 1, 0, 1)
SPINNER_ITEM_TO_FIELD = {
    "Category": "category",
    "Title": "title",
    "Year": "year",
    "Watched": "is_watched",
}
FALLBACK_SORT_KEY = "title"
# Allowed categories is different from the assignment 1
CATEGORIES = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]


class MoviesApp(App):
    """Main kivy program class"""

    sort_fields = ListProperty()
    statistics_text = StringProperty()
    state_text = StringProperty()
