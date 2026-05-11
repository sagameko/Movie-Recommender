import logging

from app.etl.load_raw_data import load_movies, load_ratings, load_tags, load_links
from app.etl.transform_data import clean_movies, clean_ratings, clean_tags
from app.etl.load_to_duckdb import load_table


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run_pipeline():
    logging.info("Starting movie recommendation data pipeline.")

    movies = load_movies()
    ratings = load_ratings()
    tags = load_tags()
    links = load_links()

    logging.info(f"Loaded movies: {len(movies)} rows.")
    logging.info(f"Loaded ratings: {len(ratings)} rows.")
    logging.info(f"Loaded tags: {len(tags)} rows.")
    logging.info(f"Loaded links: {len(links)} rows.")

    movies_clean = clean_movies(movies)
    ratings_clean = clean_ratings(ratings)
    tags_clean = clean_tags(tags)

    load_table("movies", movies_clean)
    load_table("ratings", ratings_clean)
    load_table("tags", tags_clean)
    load_table("links", links)

    logging.info("Data loaded successfully into DuckDB.")


if __name__ == "__main__":
    run_pipeline()