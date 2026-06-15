import sqlite3

DB = "procurement.db"


def mark_supplier_cannot_do(
    supplier,
    category
):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE suppliers
        SET
            cannot_do=?,
            last_response='NO'
        WHERE supplier=?
        """,
        (
            category,
            supplier
        )
    )

    conn.commit()

    conn.close()