import streamlit as st
import sqlite3
import pandas as pd

from backend.agents.outreach import save_response
from backend.agents.partner import is_partner
from backend.agents.handoff import create_handoff
from backend.agents.training import (
    mark_supplier_cannot_do
)

DB = "procurement.db"

st.title("📧 Supplier Outreach")

conn = sqlite3.connect(DB)

suppliers = pd.read_sql_query(
    """
    SELECT *
    FROM suppliers
    """,
    conn
)

conn.close()

supplier = st.selectbox(
    "Supplier",
    suppliers["supplier"]
)

commission = st.radio(
    "Commission Accepted?",
    [
        "YES",
        "NO"
    ]
)

response = st.radio(
    "Supplier Response",
    [
        "YES",
        "NO",
        "MAYBE"
    ]
)

notes = st.text_area(
    "Additional Notes"
)

if st.button("Save Response"):

    save_response(
        supplier,
        1,
        response,
        notes
    )

    # ==========================================
    # YES RESPONSE
    # ==========================================

    if response == "YES":

        if is_partner(supplier):

            create_handoff(
                supplier,
                1,
                "Existing Partner"
            )

            st.success(
                "Partner Found → Human Handoff Created"
            )

        else:

            if commission == "YES":

                create_handoff(
                    supplier,
                    1,
                    "Commission Accepted"
                )

                st.success(
                    "Commission Accepted → Human Handoff"
                )

            else:

                st.warning(
                    "Commission Rejected"
                )

    # ==========================================
    # NO RESPONSE
    # ==========================================

    elif response == "NO":

        category = st.text_input(
            "Category Supplier Cannot Do"
        )

        if category:

            mark_supplier_cannot_do(
                supplier,
                category
            )

            st.warning(
                f"{supplier} marked as unable to do {category}"
            )

        st.success(
            "NO response recorded"
        )

    # ==========================================
    # MAYBE RESPONSE
    # ==========================================

    elif response == "MAYBE":

        st.info(
            "MAYBE response recorded"
        )