import streamlit as st
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

ESCALATION_FILE = ROOT / "data" / "escalations.csv"

st.title("⚠ Escalation Monitor")

df = pd.read_csv(ESCALATION_FILE)

for _, row in df.iterrows():

    if row["Days"] >= 7:

        st.error(
            f"{row['Supplier']} - {row['Issue']} ({row['Days']} days)"
        )

    elif row["Days"] >= 5:

        st.warning(
            f"{row['Supplier']} - {row['Issue']} ({row['Days']} days)"
        )

    else:

        st.success(
            f"{row['Supplier']} - {row['Issue']} ({row['Days']} days)"
        )