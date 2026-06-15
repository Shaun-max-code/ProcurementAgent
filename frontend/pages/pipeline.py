import streamlit as st
import sqlite3
import pandas as pd

DB = "procurement.db"

st.title("🔄 Deal Pipeline")

conn = sqlite3.connect(DB)

df = pd.read_sql_query(
    """
    SELECT *
    FROM supplier_responses
    ORDER BY id DESC
    """,
    conn
)

st.dataframe(
    df,
    use_container_width=True
)

conn.close()