import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import sqlite3
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.meeting import save_meeting
from backend.agents.ai_matching import find_ai_matches

DB = ROOT / "procurement.db"

st.title("🏭 AI Supplier Matching")

# ==========================================
# LOAD LATEST REQUEST
# ==========================================

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

    if requests.empty:

        st.warning(
            "No client requests found."
        )

        st.stop()

    latest_request = requests.iloc[-1]

except Exception as e:

    st.error(
        f"Database Error: {e}"
    )

    st.stop()

# ==========================================
# SHOW REQUEST
# ==========================================

st.subheader("📋 Latest Client Request")

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"**Product:** {latest_request['product']}"
    )

    st.write(
        f"**Category:** {latest_request['category']}"
    )

with col2:

    st.write(
        f"**MOQ:** {latest_request['moq']}"
    )

    st.write(
        f"**Country:** {latest_request['country']}"
    )

st.divider()

# ==========================================
# LOAD SUPPLIERS
# ==========================================

suppliers = pd.read_sql_query(
    """
    SELECT
        supplier AS Supplier,
        category AS Category,
        moq AS MOQ,
        country AS Country
    FROM suppliers
    """,
    conn
)

conn.close()

# ==========================================
# AI MATCHING
# ==========================================

matches = find_ai_matches(
    latest_request["product"],
    suppliers
)

st.subheader("🤖 AI Supplier Recommendations")

if matches.empty:

    st.warning(
        "No suppliers found."
    )

else:

    matches["AI Score"] = (
        matches["Score"] * 100
    ).round(2)

    st.dataframe(
        matches[
            [
                "Supplier",
                "Category",
                "MOQ",
                "Country",
                "AI Score"
            ]
        ],
        use_container_width=True
    )

# ==========================================
# SELECT SUPPLIER
# ==========================================

supplier = st.selectbox(
    "Select Supplier",
    matches["Supplier"]
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