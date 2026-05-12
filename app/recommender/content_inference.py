from pathlib import Path
from typing import Optional

import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models"


def load_artifacts():
    vectorizer = joblib.load(
        MODEL_DIR / "tfidf_vectorizer.joblib"
    )

    tfidf_matrix = joblib.load(
        MODEL_DIR / "tfidf_matrix.joblib"
    )

    df = joblib.load(
        MODEL_DIR / "movie_metadata.joblib"
    )

    return vectorizer, tfidf_matrix, df


def recommend_movies(
    movie_title: str,
    limit: int = 10
) -> Optional[pd.DataFrame]:

    _, tfidf_matrix, df = load_artifacts()

    matches = df[
        df["title"].str.contains(
            movie_title,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        print(f"No movie found for: {movie_title}")
        return None

    selected_index = matches.index[0]
    selected_title = df.loc[selected_index, "title"]

    similarity_scores = cosine_similarity(
        tfidf_matrix[selected_index],
        tfidf_matrix
    ).flatten()

    result = df.copy()
    result["similarity_score"] = similarity_scores

    recommendations = (
        result[result.index != selected_index]
        .sort_values(
            "similarity_score",
            ascending=False
        )
        .head(limit)
        [[
            "title",
            "genres",
            "release_year",
            "similarity_score"
        ]]
    )

    print(f"\nBecause you searched for: {selected_title}")

    return recommendations


if __name__ == "__main__":
    recommendations = recommend_movies(
        "Toy Story",
        limit=10
    )

    if recommendations is not None:
        print(recommendations)