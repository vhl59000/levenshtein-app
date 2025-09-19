import pandas as pd

def load_words(filepath: str) -> list[str]:
    """
    Charge un fichier CSV contenant une colonne 'word' et renvoie la liste des mots.
    """
    df = pd.read_csv(filepath)
    return df["word"].tolist()

def filter_words(words: list[str], min_length: int = 5) -> list[str]:
    """
    Filtre les mots dont la longueur est >= min_length.
    """
    return [w for w in words if len(w) >= min_length]
