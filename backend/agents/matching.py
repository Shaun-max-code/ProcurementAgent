import sqlite3
import pandas as pd
from pathlib import Path
from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[2]

DB_FILE = ROOT / "procurement.db"


def find_matches(product_name):

    conn = sqlite3.connect(DB_FILE)

    suppliers = pd.read_sql_query(
        """
        SELECT
            supplier,
            category,
            moq,
            country,
            description
        FROM suppliers
        """,
        conn
    )

    conn.close()

    if suppliers.empty:
        return suppliers

    scores = []

    for _, row in suppliers.iterrows():

        supplier_text = (
            f"{row['supplier']} "
            f"{row['category']} "
            f"{row['description']} "
            f"{row['country']}"
        )

        score = max(
            fuzz.token_sort_ratio(
                product_name.lower(),
                supplier_text.lower()
            ),
            fuzz.partial_ratio(
                product_name.lower(),
                supplier_text.lower()
            )
        )

        scores.append(score)

    suppliers["match_score"] = scores

    reasons = []

    for _, row in suppliers.iterrows():

        reason = (
            f"Matches category '{row['category']}' "
            f"and specializes in "
            f"{row['description']}"
        )

        reasons.append(reason)

    suppliers["reason"] = reasons

    suppliers = suppliers.sort_values(
        by="match_score",
        ascending=False
    )

    return suppliers