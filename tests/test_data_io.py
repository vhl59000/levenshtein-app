import pandas as pd
from src.data_io import load_words, filter_words

def test_load_words(tmp_path):
    # crée un CSV temporaire
    csv_file = tmp_path / "words.csv"
    pd.DataFrame({"word": ["a", "kitten", "abc"]}).to_csv(csv_file, index=False)

    words = load_words(csv_file)
    assert "kitten" in words
    assert len(words) == 3

def test_filter_words():
    words = ["a", "kitten", "abc"]
    filtered = filter_words(words, min_length=3)
    assert filtered == ["kitten", "abc"]
