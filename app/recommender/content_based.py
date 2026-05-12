from typing import Optional

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.database.connection import get_connection


def load_content_features() -> pd.DataFrame:
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


def recommend_similar_movies(
    movie_title: str,
    limit: int = 10
) -> Optional[pd.DataFrame]:
    df = load_content_features()

    matches = df[
        df["title"].str.contains(movie_title, case=False, na=False)
    ]

    if matches.empty:
        print(f"No movie found for: {movie_title}")
        return None

    selected_index = matches.index[0]
    selected_title = df.loc[selected_index, "title"]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000
    )

    tfidf_matrix = vectorizer.fit_transform(df["content_text"].fillna(""))

    selected_vector = tfidf_matrix[selected_index]

    similarity_scores = cosine_similarity(
        selected_vector,
        tfidf_matrix
    ).flatten()

    result = df.copy()
    result["similarity_score"] = similarity_scores

    recommendations = (
        result[result.index != selected_index]
        .sort_values("similarity_score", ascending=False)
        .head(limit)
        [[
            "movie_id",
            "title",
            "genres",
            "release_year",
            "similarity_score"
        ]]
    )

    print(f"\nBecause you searched for: {selected_title}")
    return recommendations


if __name__ == "__main__":
    result = recommend_similar_movies("Toy Story", limit=10)

    if result is not None:
        print(result)