from app.database.connection import get_connection

def build_popularity_mart() -> None:
    conn = get_connection()

    conn.execute("""
        CREATE OR REPLACE TABLE mart_movie_popularity AS
        SELECT 
            m.movieId AS moview_id,
            m.title,
            m.genres,
            m.release_year,
                 
            COUNT(r.rating) AS rating_count,
            ROUND(AVG(r.rating), 2) AS avg_rating,
            
            ROUND(
                AVG(r.rating) * LOG10(COUNT(r.rating) + 1),
                2
            ) AS popularity_score
            
        FROM movies m
        LEFT JOIN ratings r
            ON m.movieId = r.movieId
                 
        GROUP BY
            m.movieId,
            m.title,
            m.genres,
            m.release_year
    """)

    conn.close()

    print("mart_movie_popularity created.")

if __name__ == "__main__":
    build_popularity_mart()