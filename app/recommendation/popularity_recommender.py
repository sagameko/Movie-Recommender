from app.database.connection import get_connection

def get_top_movies(
        limit: int=10,
        min_ratings: int = 50
):
    
    conn = get_connection()

    query = f"""
        SELECT
            title,
            genres,
            release_year,
            rating_count,
            avg_rating,
            popularity_score
        FROM mart_movie_popularity
        WHERE rating_count >= {min_ratings}
        ORDER BY popularity_score DESC
        LIMIT {limit}
    """

    df = conn.execute(query).fetchdf()

    conn.close()

    return df


if __name__ == "__main__":
    result = get_top_movies()

    print("\n Top Recommended Movies")
    print("-" *50)
    print(result)