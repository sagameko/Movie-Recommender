from pathlib import Path

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

from app.database.connection import get_connection


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)


def load_content_data():
    con = get_connection()

    df = con.execute("""
        SELECT
            movie_id,
            title,
            genres,
            release_year,
            content_text
        FROM mart_movie_content_features
    """).fetchdf()

    con.close()

    return df


def train_content_model():
    print("Loading content data...")

    df = load_content_data()

    print("Training TF-IDF vectorizer...")

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(
        df["content_text"].fillna("")
    )

    print("Saving model artifacts...")

    joblib.dump(
        vectorizer,
        MODEL_DIR / "tfidf_vectorizer.joblib"
    )

    joblib.dump(
        tfidf_matrix,
        MODEL_DIR / "tfidf_matrix.joblib"
    )

    joblib.dump(
        df,
        MODEL_DIR / "movie_metadata.joblib"
    )

    print("Content recommendation model trained successfully.")


if __name__ == "__main__":
    train_content_model()   