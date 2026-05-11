from pathlib import Path
import duckdb

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "processed" / "movies.duckdb"

def get_connection():
    """
    Create an return a DuckDB Connection

    DuckDB stores the database as a local file.
    This is good for analytics and local data science pipelines
    """

    DB_PATH.parent.mkdir(parents= True, exist_ok = True)
    return duckdb.connect(str(DB_PATH))