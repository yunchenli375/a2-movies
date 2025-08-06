"""Movie class definition"""


class Movie:
    """Represents a movie with title, year, category, and watched status"""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initializes a Movie instance with title, year, category, and watched status."""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

