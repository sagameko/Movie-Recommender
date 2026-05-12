from app.database.connection import get_connection

def build_content_features() -> None:
    con = get_connection()

    con.execute(""" 
        CREATE OR REPLACE TABLE mart_movie_content_features AS
        SELECT
            m.movieId AS movie_id,
            m.title,
            m.genres,
            m.release_year,
            COALESCE(
                STRING_AGG(DISTINCT t.tag, ' '),    
                ''
            ) AS tags,
            LOWER(
                REPLACE(m.genres, '|', ' ') || ' ' ||
                COALESCE(STRING_AGG(DISTINCT t.tag, ' '), '')
            ) AS content_text
        FROM movies m
        LEFT JOIN tags t
            ON m.movieId = t.movieId
        GROUP BY
            m.movieId,
            m.title,
            m.genres,
            m.release_year
    """)

    con.close()
    print("mart_movie_content_features created.")


if __name__ == "__main__":
    build_content_features()