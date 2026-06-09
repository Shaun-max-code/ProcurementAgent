import streamlit as st
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.followup import generate_followup

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
    """
).fetchall()

conn.close()

if not meetings:

    st.warning(
        "No completed meetings available."
    )

else:

    selected = st.selectbox(
        "Select Meeting",
        meetings,
        format_func=lambda x: f"{x[1]} → {x[2]}"
    )

    if st.button("Generate Follow-Up"):

        email = generate_followup(
            selected[1],
            selected[2]
        )

        st.text_area(
            "Generated Email",
            email,
            height=300
        )