from backend.database import get_connection
from datetime import date


def save_followup(
    supplier,
    brand
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO followups(
            supplier,
            brand,
            followup_date,
            status
        )
        VALUES(?,?,?,?)
        """,
        (
            supplier,
            brand,
            str(date.today()),
            "Sent"
        )
    )

    conn.commit()
    conn.close()


def generate_followup(
    supplier,
    brand
):

    email = f"""
Subject: Follow-Up Regarding Procurement Discussion

Dear {supplier},

We are following up regarding our procurement discussion
for {brand}.

Please provide an update regarding quotations,
availability and next steps.

Looking forward to your response.

Best Regards,
Procurement Team
"""

    return email