import streamlit as st
import sys
from pathlib import Path
import pandas as pd
from datetime import date

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.matching import find_matches
from backend.agents.meeting import save_meeting

REQUEST_DB = ROOT / "procurement.db"

st.title("🏭 Supplier Matching")

# ==========================
# LOAD LATEST REQUEST
# ==========================

try:

    import sqlite3

    conn = sqlite3.connect(REQUEST_DB)

    requests = pd.read_sql_query(
        "SELECT * FROM requests",
        conn
    )

    conn.close()

    if requests.empty:
        st.warning("No client requests found.")
        st.stop()

    latest_request = requests.iloc[-1]

except Exception as e:

    st.error(f"Error loading requests: {e}")
    st.stop()

# ==========================
# SHOW LATEST REQUEST
# ==========================

st.subheader("📋 Latest Client Request")

col1, col2 = st.columns(2)

with col1:

    st.write(f"**Product:** {latest_request['product']}")
    st.write(f"**Category:** {latest_request['category']}")

with col2:

    st.write(f"**MOQ:** {latest_request['moq']}")
    st.write(f"**Country:** {latest_request['country']}")

# ==========================
# FIND SUPPLIERS
# ==========================

matches = find_matches(
    latest_request["category"]
)

# ==========================
# DISPLAY SUPPLIERS
# ==========================

st.subheader("🎯 Matched Suppliers")

if matches.empty:

    st.warning(
        "No suppliers found for this category."
    )

else:

    st.success(
        f"{len(matches)} supplier(s) found"
    )

    st.dataframe(
        matches,
        use_container_width=True
    )

# ==========================
# SCHEDULE MEETING
# ==========================

if not matches.empty:

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