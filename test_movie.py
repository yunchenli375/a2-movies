"""(Incomplete) Tests for Movie class."""

from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert default_movie.is_watched is False

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    # TODO: Write tests to show this initialisation works
    print("Test initial-value movie:")
    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.year == 2017
    assert initial_movie.category == "Comedy"
    assert initial_movie.is_watched is True

