import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.escalation import generate_escalations

st.title("⚠️ Escalation Monitor")

alerts = generate_escalations()

if not alerts:

    st.success("✅ No escalations found")

else:

    st.subheader("Active Escalations")

    for supplier, issue, severity in alerts:

        if severity == "High":

            st.error(
                f"{supplier} - {issue}"
            )

        elif severity == "Medium":

            st.warning(
                f"{supplier} - {issue}"
            )

        else:

            st.success(
                f"{supplier} - {issue}"
            )