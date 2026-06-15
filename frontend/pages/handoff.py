import streamlit as st
import sqlite3
import pandas as pd

DB = "procurement.db"

st.title("🤝 Human Handoffs")

conn = sqlite3.connect(DB)

df = pd.read_sql_query(
    """
    SELECT *
    FROM human_handoffs
    ORDER BY id DESC
    """,
    conn
)

conn.close()

st.dataframe(
    df,
    use_container_width=True
)