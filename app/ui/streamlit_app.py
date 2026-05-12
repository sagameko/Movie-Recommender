import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import plotly.express as px

from app.database.connection import get_connection
from app.recommender.content_inference import recommend_movies


st.set_page_config(
    page_title="Movie Recommendation Platform",
    layout="wide"
)


@st.cache_data
def load_movie_data():
    con = get_connection()

    df = con.execute("""
        SELECT
            movie_id,
            title,
            genres,
            release_year,
            rating_count,
            avg_rating
        FROM mart_movie_ratings
    """).fetchdf()

    con.close()

    return df


def show_overview(df):
    st.title("Movie Recommendation & Analytics Platform")

    total_movies = df["movie_id"].nunique()

    rated_movies = df[
        df["rating_count"] > 0
    ]["movie_id"].nunique()

    average_rating = round(
        df["avg_rating"].mean(),
        2
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Movies",
        f"{total_movies:,}"
    )

    col2.metric(
        "Movies With Ratings",
        f"{rated_movies:,}"
    )

    col3.metric(
        "Average Rating",
        average_rating
    )

    st.subheader("Top Rated Movies")

    top_movies = (
        df[df["rating_count"] >= 50]
        .sort_values(
            "avg_rating",
            ascending=False
        )
        .head(20)
    )

    st.dataframe(
        top_movies,
        use_container_width=True
    )


def show_analytics(df):
    st.title("Movie Analytics")

    st.subheader("Rating Distribution")

    fig = px.histogram(
        df.dropna(subset=["avg_rating"]),
        x="avg_rating",
        nbins=20,
        title="Average Rating Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Movies By Release Year")

    yearly_movies = (
        df.dropna(subset=["release_year"])
        .groupby("release_year")
        .size()
        .reset_index(name="movie_count")
        .sort_values("release_year")
    )

    fig2 = px.line(
        yearly_movies,
        x="release_year",
        y="movie_count",
        title="Movies Released Per Year"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


def show_recommendations(df):
    st.title("Movie Recommendations")

    movie_titles = sorted(
        df["title"]
        .dropna()
        .unique()
    )

    selected_movie = st.selectbox(
        "Choose a movie",
        movie_titles
    )

    limit = st.slider(
        "Number of Recommendations",
        min_value=5,
        max_value=20,
        value=10
    )

    if st.button("Get Recommendations"):
        recommendations = recommend_movies(
            selected_movie,
            limit=limit
        )

        if recommendations is None or recommendations.empty:
            st.warning("No recommendations found for this movie. Try another title.")
        else:
            st.subheader(f"Movies Similar To: {selected_movie}")
            st.dataframe(
                recommendations,
                width="stretch"
            )

def main():
    df = load_movie_data()

    page = st.sidebar.radio(
        "Navigation",
        [
            "Overview",
            "Analytics",
            "Recommendations"
        ]
    )

    if page == "Overview":
        show_overview(df)

    elif page == "Analytics":
        show_analytics(df)

    elif page == "Recommendations":
        show_recommendations(df)


if __name__ == "__main__":
    main()