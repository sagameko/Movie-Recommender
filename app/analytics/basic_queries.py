from app.database.connection import get_connection


def run_basic_queries():
    con = get_connection()

    print("\nTop 10 highest rated movies:")
    result = con.execute("""
        SELECT
            m.title,
            COUNT(r.rating) AS rating_count,
            ROUND(AVG(r.rating), 2) AS avg_rating
        FROM ratings r
        JOIN movies m
            ON r.movieId = m.movieId
        GROUP BY m.title
        HAVING COUNT(r.rating) >= 50
        ORDER BY avg_rating DESC
        LIMIT 10
    """).fetchdf()

    print(result)

    con.close()


if __name__ == "__main__":
    run_basic_queries()