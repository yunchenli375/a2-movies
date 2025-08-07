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

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.collection = MovieCollection()
        self.collection.load_movies(DATA_FILE_JSON)
        self.sort_fields = list(SPINNER_ITEM_TO_FIELD.keys())
        self.state_text = ""
        self.statistics_text = self.collection.get_statistics_info()
        self.sort_key = FALLBACK_SORT_KEY

    def build(self):
        """Build the GUI"""
        self.title = PROGRAM_NAME
        self.root = Builder.load_file(GUI_LAYOUT)
        self.refresh_dynamic_widgets()
        return self.root

    def refresh_dynamic_widgets(self):
        """add buttons for each movie in the collection"""
        self.root.ids.container.clear_widgets()
        self.collection.sort(self.sort_key)
        for i, movie in enumerate(self.collection.movies):
            entry = Button(text=str(movie))
            entry.background_color = (
                COLOR_WATCHED if movie.is_watched else COLOR_UNWATCHED
            )
            entry.bind(on_press=self.on_movie_button_press)
            entry.collection_index = i
            self.root.ids.container.add_widget(entry)

