# Movie Recommendation System

A production-style movie recommendation system built with Python, DuckDB, SQL-based feature engineering, and machine learning techniques.

This project demonstrates how a real-world recommendation pipeline can be structured using modular data engineering and machine learning practices rather than a single notebook workflow.

The system uses content-based filtering with TF-IDF vectorization and cosine similarity to recommend similar movies based on genres and user-generated tags.

---

# Project Objectives

The purpose of this project is to:

- Build a modular recommendation pipeline
- Practice real-world data engineering structure
- Learn feature engineering for NLP systems
- Implement content-based recommendation algorithms
- Create a deployable machine learning application
- Simulate industry-style analytics architecture

---

# Features

- Movie metadata ingestion pipeline
- SQL-based feature engineering marts
- DuckDB analytical database integration
- TF-IDF vectorization
- Cosine similarity recommendation engine
- Interactive Streamlit application
- Modular project structure
- Reusable recommendation logic

---

# Technologies Used

## Programming & Data

- Python
- Pandas
- SQL
- DuckDB

## Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## Application Layer

- Streamlit

---

# Project Structure

```text
movie-recommend/
│
├── app/
│   ├── analytics/
│   ├── database/
│   ├── etl/
│   ├── marts/
│   ├── recommender/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── tests/
│
├── streamlit_app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Architecture Overview

```text
Raw Movie Data
        ↓
ETL Pipeline
        ↓
DuckDB Storage
        ↓
Feature Engineering Mart
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity Engine
        ↓
Movie Recommendations
        ↓
Streamlit Frontend
```

---

# Recommendation Logic

The system combines:

- movie genres
- user-generated tags

into a single text feature called `content_text`.

Example:

```text
action adventure sci-fi alien future space war
```

This text is transformed using TF-IDF vectorization into numerical feature vectors.

Cosine similarity is then used to calculate similarity scores between movies.

---

# Example Recommendation Flow

```python
recommend_movies(
    movie_title="Toy Story",
    top_n=10
)
```

Example output:

```text
Toy Story 2
A Bug's Life
Antz
Monsters, Inc.
Finding Nemo
```

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd movie-recommend
```

---

## 2. Create Environment

Using Conda:

```bash
conda create -n movie_rec python=3.11
conda activate movie_rec
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Data Pipeline

```bash
python main.py
```

This will:

- load raw datasets
- build analytical marts
- create movie content features

---

## 5. Launch Streamlit App

```bash
streamlit run streamlit_app.py
```

---

# Learning Outcomes

This project helped develop practical skills in:

- data engineering workflows
- feature engineering
- recommendation systems
- NLP vectorization
- analytical database design
- modular Python architecture
- application deployment concepts

---

# Future Improvements

Planned enhancements include:

- Hybrid recommendation system
- Collaborative filtering
- User-based recommendations
- Embedding-based similarity search
- FastAPI backend service
- Docker containerization
- Cloud deployment
- Recommendation explainability
- Movie poster integration
- User authentication
- Real-time recommendation APIs

---

# Why This Project Matters

Many machine learning projects focus only on model training inside notebooks.

This project focuses on building a more complete system that resembles real-world machine learning and analytics engineering workflows:

- ETL pipelines
- analytical marts
- reusable ML modules
- application integration
- deployable architecture

The goal is not only to build a recommendation model, but also to understand how machine learning systems are structured in production environments.

---

# Dataset

This project uses the MovieLens dataset.

Source:
https://grouplens.org/datasets/movielens/

---

# Author

Duong Nguyen

Master of Data Science  
Swinburne University of Technology  
Melbourne, Australia