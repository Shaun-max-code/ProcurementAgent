import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DB_FILE = ROOT / "procurement.db"


def find_matches(category):

    conn = sqlite3.connect(DB_FILE)

    query = """
    SELECT
        supplier,
        category,
        moq,
        country
    FROM suppliers
    WHERE category = ?
    """

    matches = pd.read_sql_query(
        query,
        conn,
        params=(category,)
    )

    conn.close()

    return matches