import pandas as pd


def clean_movies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["title"] = df["title"].astype(str).str.strip()
    df["genres"] = df["genres"].astype(str).str.strip()

    # Extract release year from title, for example Toy Story (1995)
    df["release_year"] = df["title"].str.extract(r"\((\d{4})\)")
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")

    return df


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["rating_timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    df = df.drop(columns=["timestamp"])

    return df


def clean_tags(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["tag"] = df["tag"].astype(str).str.strip().str.lower()
    df["tag_timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

    df = df.drop(columns=["timestamp"])

    return df