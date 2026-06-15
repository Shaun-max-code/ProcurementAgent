from backend.database import get_connection


def save_request(product, category, moq, country):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO requests
        (product, category, moq, country)
        VALUES (?, ?, ?, ?)
        """,
        (product, category, moq, country)
    )

    conn.commit()
    conn.close()

    return True