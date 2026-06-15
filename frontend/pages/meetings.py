import streamlit as st
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "procurement.db"

st.title("📅 Meeting Coordination")

conn = sqlite3.connect(DB)

meetings = conn.execute(
    """
    SELECT
        id,
        brand,
        supplier,
        meeting_date,
        status
    FROM meetings
    ORDER BY id DESC
    """
).fetchall()

conn.close()

if not meetings:

    st.warning("No meetings scheduled yet.")

else:

    st.subheader("Scheduled Meetings")

    for meeting in meetings:

        col1, col2 = st.columns([4,1])

        with col1:

            st.info(
                f"""
Brand: {meeting[1]}

Supplier: {meeting[2]}

Date: {meeting[3]}

Status: {meeting[4]}
"""
            )

        with col2:

            if st.button(
                "Complete",
                key=f"complete_{meeting[0]}"
            ):

                conn = sqlite3.connect(DB)

                conn.execute(
                    """
                    UPDATE meetings
                    SET status='Completed'
                    WHERE id=?
                    """,
                    (meeting[0],)
                )

                conn.commit()
                conn.close()

                st.rerun()