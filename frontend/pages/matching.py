import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import sqlite3
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.matching import find_matches
from backend.agents.meeting import save_meeting

DB = ROOT / "procurement.db"

st.title("🏭 AI-Powered Supplier Matching")

try:
    conn = sqlite3.connect(DB)

    requests = pd.read_sql_query(
        """
        SELECT *
        FROM requests
        ORDER BY id DESC
        """,
        conn
    )

    conn.close()

    if requests.empty:
        st.warning("No client requests found.")
        st.stop()

    latest_request = requests.iloc[-1]

except Exception as e:
    st.error(f"Database Error: {e}")
    st.stop()

st.subheader("📋 Latest Client Request")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Product:** {latest_request['product']}")
    st.write(f"**Category:** {latest_request['category']}")

with col2:
    st.write(f"**MOQ:** {latest_request['moq']}")
    st.write(f"**Country:** {latest_request['country']}")

st.divider()

matches = find_matches(
    latest_request["product"]
)

st.subheader("🤖 AI-Powered Supplier Recommendations")

if matches.empty:

    st.warning("No suppliers found.")

else:

    matches["match_score"] = (
        matches["match_score"]
        .round(0)
        .astype(int)
    )

    st.dataframe(
        matches[
            [
                "supplier",
                "category",
                "description",
                "country",
                "match_score"
            ]
        ],
        use_container_width=True
    )

    st.subheader("💡 Why These Matches?")

    for _, row in matches.head(3).iterrows():

        st.info(
            f"""
Supplier: {row['supplier']}

Score: {row['match_score']}%

Reason:
{row['reason']}
"""
        )

    st.divider()

    best_supplier = matches.iloc[0]

    st.success(
        f"""
🏆 Best Match

Supplier: {best_supplier['supplier']}

Match Score: {best_supplier['match_score']}%
"""
    )

    supplier = st.selectbox(
        "Select Supplier",
        matches["supplier"]
    )

    if st.button("📅 Schedule Meeting"):

        save_meeting(
            latest_request["product"],
            supplier,
            str(date.today())
        )

        st.success(
            f"Meeting scheduled with {supplier}"
        )