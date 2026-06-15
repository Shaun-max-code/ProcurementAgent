import sqlite3

DB = "procurement.db"


def add_competitor(
    competitor,
    manufacturer,
    confidence_score
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO competitors
        (
            competitor,
            manufacturer,
            confidence_score
        )
        VALUES (?, ?, ?)
        """,
        (
            competitor,
            manufacturer,
            confidence_score
        )
    )

    conn.commit()

    conn.close()