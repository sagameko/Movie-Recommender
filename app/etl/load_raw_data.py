from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw" / "ml-latest"

def load_movies() -> pd.DataFrame:
    path = RAW_DIR / "movies.csv"
    return pd.read_csv(path)


def load_ratings() -> pd.DataFrame:
    path = RAW_DIR / "ratings.csv"
    return pd.read_csv(path)


def load_tags() -> pd.DataFrame:
    path = RAW_DIR / "tags.csv"
    return pd.read_csv(path)


def load_links() -> pd.DataFrame:
    path = RAW_DIR / "links.csv"
    return pd.read_csv(path)