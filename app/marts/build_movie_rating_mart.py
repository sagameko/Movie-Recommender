from app.database.connection import get_connection


def build_movie_rating_mart() -> None:
    con = get_connection()

    con.execute("""
        CREATE OR REPLACE TABLE mart_movie_ratings AS
        SELECT
            m.movieId AS movie_id,
            m.title,
            m.genres,
            m.release_year,
            COUNT(r.rating) AS rating_count,
            ROUND(AVG(r.rating), 2) AS avg_rating,
            MIN(r.rating_timestamp) AS first_rating_at,
            MAX(r.rating_timestamp) AS last_rating_at
        FROM movies m
        LEFT JOIN ratings r
            ON m.movieId = r.movieId
        GROUP BY
            m.movieId,
            m.title,
            m.genres,
            m.release_year
    """)

    con.close()
    print("mart_movie_ratings created successfully.")


if __name__ == "__main__":
    build_movie_rating_mart()