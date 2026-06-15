from backend.database import get_connection


def save_meeting(brand, supplier, meeting_date):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO meetings
        (brand, supplier, meeting_date, status)
        VALUES (?, ?, ?, ?)
        """,
        (
            brand,
            supplier,
            meeting_date,
            "Pending"
        )
    )

    conn.commit()
    conn.close()

    return True