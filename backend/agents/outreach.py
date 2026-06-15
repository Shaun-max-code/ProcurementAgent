import sqlite3
from datetime import date

DB = "procurement.db"


def save_response(
    supplier,
    request_id,
    response,
    notes=""
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO supplier_responses
        (
            supplier,
            request_id,
            response,
            notes,
            response_date,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            supplier,
            request_id,
            response,
            notes,
            str(date.today()),
            "Open"
        )
    )

    conn.commit()

    conn.close()