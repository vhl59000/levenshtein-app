import pytest
from src.levenshtein import levenshtein_distance

@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("", "", 0),
        ("a", "", 1),
        ("", "abc", 3),
        ("kitten", "sitting", 3),
        ("flaw", "lawn", 2),
        ("gumbo", "gambol", 2),
        ("distance", "instance", 2),
    ],
)
def test_levenshtein_distance(s1, s2, expected):
    assert levenshtein_distance(s1, s2) == expected
