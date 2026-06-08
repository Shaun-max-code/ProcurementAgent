import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# ==========================
# PROJECT ROOT
# ==========================

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.matching import find_matches

# ==========================
# PAGE TITLE
# ==========================

st.title("🏭 Supplier Matching")

# ==========================
# LOAD LATEST CLIENT REQUEST
# ==========================

REQUEST_FILE = ROOT / "data" / "client_requests.csv"

try:

    requests = pd.read_csv(REQUEST_FILE)

    if requests.empty:
        st.warning("No client requests found.")
        st.stop()

    latest_request = requests.iloc[-1]

except Exception as e:

    st.error(f"Error loading requests: {e}")
    st.stop()

# ==========================
# DISPLAY LATEST REQUEST
# ==========================

st.subheader("📋 Latest Client Request")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Product:** {latest_request['Product']}")
    st.write(f"**Category:** {latest_request['Category']}")

with col2:
    st.write(f"**MOQ:** {latest_request['MOQ']}")
    st.write(f"**Country:** {latest_request['Country']}")

# ==========================
# FIND MATCHING SUPPLIERS
# ==========================

category = latest_request["Category"]

matches = find_matches(category)

# ==========================
# DISPLAY MATCHES
# ==========================

st.subheader("🎯 Matched Suppliers")

if matches.empty:

    st.warning("No suppliers found for this category.")

else:

    st.success(f"{len(matches)} supplier(s) found")

    st.dataframe(
        matches,
        use_container_width=True
    )

# ==========================
# SUPPLIER SELECTION
# ==========================

if not matches.empty:

    supplier = st.selectbox(
        "Select Supplier",
        matches["Supplier"]
    )

    if st.button("📅 Schedule Meeting"):

        st.success(
            f"Meeting request generated for {supplier}"
        )