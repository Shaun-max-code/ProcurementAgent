# frontend/pages/meetings.py

import streamlit as st

st.title("📅 Meeting Coordination")

brand = st.text_input("Brand Name")

supplier = st.text_input("Supplier")

date = st.date_input("Meeting Date")

if st.button("Generate Meeting Request"):

    st.success("Meeting Draft Generated")

    st.text_area(
        "Email",
        f"""
Hello {supplier},

We would like to schedule a meeting regarding collaboration opportunities.

Meeting Date:
{date}

Regards,
{brand}
        """,
        height=250
    )