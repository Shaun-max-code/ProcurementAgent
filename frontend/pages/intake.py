# frontend/pages/intake.py

import streamlit as st

st.title("📋 Client Intake")

with st.form("client_form"):

    product = st.text_input("Product Name")
    category = st.text_input("Category")
    moq = st.number_input("MOQ", min_value=0)
    country = st.text_input("Country")

    submit = st.form_submit_button("Submit")

if submit:

    st.success("Client Request Submitted")

    st.json({
        "Product": product,
        "Category": category,
        "MOQ": moq,
        "Country": country
    })