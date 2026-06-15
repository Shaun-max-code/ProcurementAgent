import sqlite3
from datetime import date

DB = "procurement.db"


def save_email(
    supplier,
    product,
    email_type,
    email_content
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO emails
        (
            supplier,
            product,
            email_type,
            email_content,
            created_date
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            supplier,
            product,
            email_type,
            email_content,
            str(date.today())
        )
    )

    conn.commit()

    conn.close()