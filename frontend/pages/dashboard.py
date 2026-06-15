import streamlit as st
import sqlite3
import pandas as pd
import sys
from pathlib import Path
import plotly.express as px

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from backend.agents.escalation import generate_escalations

DB = ROOT / "procurement.db"

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Procurement Dashboard")
st.markdown("Welcome to the Procurement AI Platform")

# ==========================
# DATABASE CONNECTION
# ==========================

conn = sqlite3.connect(DB)

# ==========================
# COUNTS
# ==========================

try:
    requests_count = conn.execute(
        "SELECT COUNT(*) FROM requests"
    ).fetchone()[0]
except:
    requests_count = 0

try:
    suppliers_count = conn.execute(
        "SELECT COUNT(*) FROM suppliers"
    ).fetchone()[0]
except:
    suppliers_count = 0

try:
    meetings_count = conn.execute(
        "SELECT COUNT(*) FROM meetings"
    ).fetchone()[0]
except:
    meetings_count = 0

try:
    escalations_count = len(
        generate_escalations()
    )
except:
    escalations_count = 0

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏢 Client Requests",
        requests_count
    )

with col2:
    st.metric(
        "🏭 Suppliers",
        suppliers_count
    )

with col3:
    st.metric(
        "📅 Meetings",
        meetings_count
    )

with col4:
    st.metric(
        "⚠ Escalations",
        escalations_count
    )

st.divider()

# ==========================
# WORKFLOW STATUS
# ==========================

st.subheader("🔄 Workflow Status")

workflow_data = pd.DataFrame({
    "Stage": [
        "Client Intake",
        "Supplier Database",
        "Meeting Coordination",
        "Escalation Monitoring"
    ],
    "Count": [
        requests_count,
        suppliers_count,
        meetings_count,
        escalations_count
    ]
})

st.dataframe(
    workflow_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================
# RECENT REQUESTS
# ==========================

st.subheader("📌 Recent Requests")

try:

    recent_requests = pd.read_sql_query(
        """
        SELECT product,
               category,
               country
        FROM requests
        ORDER BY id DESC
        LIMIT 5
        """,
        conn
    )

    if recent_requests.empty:

        st.info("No requests yet.")

    else:

        for _, row in recent_requests.iterrows():

            st.success(
                f"{row['product']} | "
                f"{row['category']} | "
                f"{row['country']}"
            )

except Exception as e:

    st.warning(str(e))

st.divider()

st.subheader("📊 Requests By Category")

try:

    category_data = pd.read_sql_query(
        """
        SELECT
            category,
            COUNT(*) as total
        FROM requests
        GROUP BY category
        """,
        conn
    )

    if not category_data.empty:

      fig = px.bar(
    category_data,
    x="category",
    y="total",
    text="total",
    title="Requests By Category"
)

      fig.update_layout(
    height=400,
    xaxis_title="Category",
    yaxis_title="Requests",
    showlegend=False
)

      st.plotly_chart(
      fig,
      use_container_width=True
)

except Exception as e:

    st.warning(
        f"Chart Error: {e}"
    )

    st.subheader("📅 Meetings By Status")

try:

    meeting_data = pd.read_sql_query(
        """
        SELECT
            status,
            COUNT(*) as total
        FROM meetings
        GROUP BY status
        """,
        conn
    )

    if not meeting_data.empty:

        fig = px.pie(
            meeting_data,
            names="status",
            values="total",
            title="Meetings By Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

except Exception as e:

    st.warning(
        f"Chart Error: {e}"
    )

st.subheader("🌎 Suppliers By Country")

try:

    supplier_data = pd.read_sql_query(
        """
        SELECT
            country,
            COUNT(*) as total
        FROM suppliers
        GROUP BY country
        """,
        conn
    )

    if not supplier_data.empty:

        fig = px.bar(
            supplier_data,
            x="country",
            y="total",
            title="Suppliers By Country"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

except Exception as e:

    st.warning(
        f"Chart Error: {e}"
    )

# ==========================
# TOP SUPPLIERS
# ==========================

st.subheader("🏭 Supplier Database")

try:

    suppliers = pd.read_sql_query(
        """
        SELECT supplier,
               category,
               moq,
               country
        FROM suppliers
        LIMIT 10
        """,
        conn
    )

    st.dataframe(
        suppliers,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:

    st.warning(str(e))

st.divider()

# ==========================
# ACTIVE ESCALATIONS
# ==========================

st.subheader("⚠ Active Escalations")

alerts = generate_escalations()

if not alerts:

    st.success(
        "No active escalations"
    )

else:

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

            st.info(
                f"{supplier} - {issue}"
            )

st.divider()

# ==========================
# RECENT MEETINGS
# ==========================

st.subheader("📅 Recent Meetings")

try:

    meetings = pd.read_sql_query(
        """
        SELECT brand,
               supplier,
               meeting_date,
               status
        FROM meetings
        ORDER BY id DESC
        LIMIT 5
        """,
        conn
    )

    st.dataframe(
        meetings,
        use_container_width=True,
        hide_index=True
    )

except Exception as e:

    st.warning(str(e))

st.divider()

# ==========================
# SYSTEM STATUS
# ==========================

st.subheader("⚙️ System Status")

st.success(
    "✅ Procurement AI Platform Online"
)

conn.close()