"""(Incomplete) Tests for MovieCollection class."""

from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert movie_collection.movies == []

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies("movies.json")
    print(movie_collection)
    assert (
        movie_collection.movies
    )  # Assuming file is non-empty; non-empty list is considered True

