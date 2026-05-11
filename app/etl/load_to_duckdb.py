from app.database.connection import get_connection


def load_table(table_name: str, df):
    con = get_connection()

    con.register("temp_df", df)

    con.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT *
        FROM temp_df
    """)

    con.close()