import sqlite3

DB = "procurement.db"


def create_handoff(
    supplier,
    request_id,
    notes
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO human_handoffs
        (
            supplier,
            request_id,
            status,
            notes
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            supplier,
            request_id,
            "Ready For Human",
            notes
        )
    )

    conn.commit()

    conn.close()