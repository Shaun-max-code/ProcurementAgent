import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.intake import save_request

st.title("📋 Client Intake")

with st.form("client_form"):

    product = st.text_input("Product Name")
    category = st.text_input("Category")
    moq = st.number_input("MOQ", min_value=0)
    country = st.text_input("Country")

    submit = st.form_submit_button("Submit")

if submit:

    save_request(
        product,
        category,
        moq,
        country
    )

    st.success("✅ Request Saved Successfully")