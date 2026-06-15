import streamlit as st

from backend.agents.email_generator import (
    generate_email
)
from backend.agents.email_storage import (
    save_email
)

st.title("✉️ Email Generator Center")

supplier = st.text_input(
    "Supplier Name"
)

product = st.text_input(
    "Product Name"
)

email_type = st.selectbox(
    "Email Type",
    [
        "OUTREACH",
        "YES",
        "NO",
        "MAYBE",
        "FOLLOWUP",
        "ESCALATION"
    ]
)

if st.button("Generate Email"):

    email = generate_email(
        email_type,
        supplier,
        product
    )

    save_email(
        supplier,
        product,
        email_type,
        email
    )

    st.text_area(
        "Generated Email",
        email,
        height=400
    )