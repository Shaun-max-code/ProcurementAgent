import streamlit as st
import sqlite3
import pandas as pd

from backend.agents.competitor import add_competitor

DB = "procurement.db"

st.title("🏭 Competitor Discovery")

competitor = st.text_input(
    "Competitor Brand"
)

manufacturer = st.text_input(
    "Possible Manufacturer"
)

confidence = st.slider(
    "Confidence",
    0,
    100,
    80
)

if st.button("Add Discovery"):

    add_competitor(
        competitor,
        manufacturer,
        confidence
    )

    st.success(
        "Competitor manufacturer added"
    )

conn = sqlite3.connect(DB)

df = pd.read_sql_query(
    """
    SELECT *
    FROM competitors
    ORDER BY id DESC
    """,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

conn.close()