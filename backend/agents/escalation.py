import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "procurement.db"


def generate_escalations():

    conn = sqlite3.connect(DB)

    meetings = conn.execute(
        """
        SELECT supplier,
               meeting_date,
               status
        FROM meetings
        """
    ).fetchall()

    conn.close()

    alerts = []

    today = datetime.today()

    for supplier, meeting_date, status in meetings:

        if status == "Pending":

            days = (
                today -
                datetime.strptime(
                    meeting_date,
                    "%Y-%m-%d"
                )
            ).days

            if days > 7:

                alerts.append(
                    (
                        supplier,
                        f"Meeting pending for {days} days",
                        "High"
                    )
                )

            elif days > 3:

                alerts.append(
                    (
                        supplier,
                        f"Meeting pending for {days} days",
                        "Medium"
                    )
                )

    return alerts