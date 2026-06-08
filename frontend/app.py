import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="AI Procurement Agent",
    layout="wide"
)

# Title
st.title("🚀 AI Procurement Agent")
st.subheader("Client Intake Form")

# Form
with st.form("client_form"):
    product = st.text_input("Product Name")
    category = st.text_input("Category")
    moq = st.number_input("MOQ", min_value=0)
    price = st.number_input("Target Price ($)", min_value=0.0)
    country = st.text_input("Country")

    submitted = st.form_submit_button("Submit")

# Show submitted data
if submitted:

  if submitted:

    st.success("Request Captured!")

    st.json({
        "product": product,
        "category": category,
        "moq": moq,
        "price": price,
        "country": country
    })

    suppliers = pd.read_csv("suppliers.csv")

    matches = suppliers[
        suppliers["Category"].str.lower() == category.lower()
    ]

    st.subheader("🏭 Recommended Suppliers")

    if len(matches) > 0:
        st.dataframe(matches)
    else:
        st.warning("No suppliers found.")