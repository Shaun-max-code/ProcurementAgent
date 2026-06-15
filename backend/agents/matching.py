import sqlite3
import pandas as pd
from pathlib import Path
from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[2]

DB_FILE = ROOT / "procurement.db"



def find_matches(
    product_name,
    category,
    country,
    moq
):

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

    # Filter suppliers by category first
    suppliers = suppliers[
        suppliers["category"].str.lower()
        == category.lower()
    ]

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

        description_score = max(
            fuzz.token_sort_ratio(
                product_name.lower(),
                supplier_text.lower()
            ),
            fuzz.partial_ratio(
                product_name.lower(),
                supplier_text.lower()
            )
        )

        score = 0

        # Category Match
        if row["category"].lower() == category.lower():
            score += 50

        # Country Match
        if row["country"].lower() == country.lower():
            score += 20

        # MOQ Match
        if row["moq"] >= moq:
            score += 15

        # Description Similarity
        score += description_score * 0.15

        score = min(score, 100)

        scores.append(round(score, 2))

    suppliers["match_score"] = scores

    reasons = []

    for _, row in suppliers.iterrows():

        reason = (
            f"Matches category '{row['category']}', "
            f"supports MOQ {row['moq']}, "
            f"located in {row['country']} and "
            f"specializes in {row['description']}"
        )

        reasons.append(reason)

    suppliers["reason"] = reasons

    suppliers = suppliers.sort_values(
        by="match_score",
        ascending=False
    )

    return suppliers