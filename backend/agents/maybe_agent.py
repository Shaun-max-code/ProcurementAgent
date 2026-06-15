import sqlite3
import pandas as pd

DB = "procurement.db"


def get_maybe_questions():

    conn = sqlite3.connect(DB)

    df = pd.read_sql_query(
        """
        SELECT *
        FROM supplier_responses
        WHERE response='MAYBE'
        """,
        conn
    )

    conn.close()

    return df


def unique_questions():

    df = get_maybe_questions()

    if df.empty:
        return []

    questions = []

    for q in df["notes"]:

        q = str(q).strip()

        if q not in questions:

            questions.append(q)

    return questions