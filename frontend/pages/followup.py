import streamlit as st
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.followup import (
    generate_followup,
    save_followup
)

DB = ROOT / "procurement.db"

st.title("✉️ Follow-Up Generator")

conn = sqlite3.connect(DB)

meetings = conn.execute(
    """
    SELECT
        id,
        brand,
        supplier
    FROM meetings
    WHERE status='Completed'
    ORDER BY id DESC
    """
).fetchall()

conn.close()

if not meetings:

    st.warning(
        "No completed meetings found."
    )

else:

    selected = st.selectbox(
        "Select Meeting",
        meetings,
        format_func=lambda x:
        f"{x[1]} → {x[2]}"
    )

    if st.button(
        "Generate Follow-Up"
    ):

        email = generate_followup(
            selected[2],
            selected[1]
        )

        save_followup(
            selected[2],
            selected[1]
        )

        st.success(
            "Follow-Up Saved Successfully"
        )

        st.text_area(
            "Generated Follow-Up Email",
            email,
            height=300
        )