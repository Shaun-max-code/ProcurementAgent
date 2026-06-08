# frontend/pages/matching.py

import streamlit as st
import pandas as pd

st.title("🏭 Supplier Matching")

try:

    suppliers = pd.read_csv("../data/suppliers.csv")

    st.dataframe(
        suppliers,
        use_container_width=True
    )

except:

    st.warning("suppliers.csv not found")