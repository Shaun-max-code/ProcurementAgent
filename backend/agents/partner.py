import sqlite3

DB = "procurement.db"


def is_partner(supplier):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM partners
        WHERE supplier=?
        """,
        (supplier,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def add_partner(
    supplier,
    commission="YES"
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO partners
        (
            supplier,
            commission_partner
        )
        VALUES (?, ?)
        """,
        (
            supplier,
            commission
        )
    )

    conn.commit()

    conn.close()