import streamlit as st
import sqlite3
from pathlib import Path
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Procurement AI Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# DATABASE
# ==========================================

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "procurement.db"

conn = sqlite3.connect(DB)

# ==========================================
# KPI DATA
# ==========================================

try:
    request_count = conn.execute(
        "SELECT COUNT(*) FROM requests"
    ).fetchone()[0]
except:
    request_count = 0

try:
    supplier_count = conn.execute(
        "SELECT COUNT(*) FROM suppliers"
    ).fetchone()[0]
except:
    supplier_count = 0

try:
    meeting_count = conn.execute(
        "SELECT COUNT(*) FROM meetings"
    ).fetchone()[0]
except:
    meeting_count = 0

try:
    escalation_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM escalations
        WHERE status='Open'
        """
    ).fetchone()[0]
except:
    escalation_count = 0

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3050/3050525.png",
    width=100
)

st.sidebar.markdown("## Procurement AI")
st.sidebar.markdown("---")

# ==========================================
# HERO SECTION
# ==========================================

st.title("🚀 Procurement AI Platform")

st.markdown("""
### AI-Powered Supplier Discovery & Procurement Automation

Manage your entire procurement lifecycle using intelligent supplier discovery,
automated supplier matching, meeting coordination,
follow-up generation and escalation monitoring.
""")

st.divider()

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📋 Requests",
        request_count
    )

with col2:
    st.metric(
        "🏭 Suppliers",
        supplier_count
    )

with col3:
    st.metric(
        "📅 Meetings",
        meeting_count
    )

with col4:
    st.metric(
        "⚠️ Escalations",
        escalation_count
    )

st.divider()

# ==========================================
# QUICK ACCESS
# ==========================================

st.subheader("⚡ Quick Access")

col1, col2, col3 = st.columns(3)

with col1:

    st.page_link(
        "pages/dashboard.py",
        label="📊 Dashboard"
    )

    st.page_link(
        "pages/intake.py",
        label="📋 Client Intake"
    )

with col2:

    st.page_link(
        "pages/matching.py",
        label="🏭 Supplier Matching"
    )

    st.page_link(
        "pages/meetings.py",
        label="📅 Meeting Coordination"
    )

with col3:

    st.page_link(
        "pages/followup.py",
        label="✉️ Follow-Ups"
    )

    st.page_link(
        "pages/escalations.py",
        label="⚠️ Escalations"
    )

st.divider()

# ==========================================
# WORKFLOW SUMMARY
# ==========================================

st.subheader("🔄 Workflow Summary")

workflow_df = pd.DataFrame({
    "Stage": [
        "Client Intake",
        "Supplier Matching",
        "Meeting Coordination"
    ],
    "Count": [
        request_count,
        supplier_count,
        meeting_count
    ]
})

st.dataframe(
    workflow_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================
# RECENT REQUESTS
# ==========================================

st.subheader("📋 Recent Requests")

try:

    requests = conn.execute(
        """
        SELECT product,
               category,
               country
        FROM requests
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    if requests:

        for req in requests:

            st.info(
                f"Product: {req[0]} | Category: {req[1]} | Country: {req[2]}"
            )

    else:

        st.warning(
            "No requests available."
        )

except:

    st.warning(
        "No request data found."
    )

st.divider()

# ==========================================
# RECENT MEETINGS
# ==========================================

st.subheader("📅 Recent Meetings")

try:

    meetings = conn.execute(
        """
        SELECT brand,
               supplier,
               meeting_date,
               status
        FROM meetings
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    if meetings:

        for meeting in meetings:

            st.success(
                f"{meeting[0]} → {meeting[1]} | {meeting[3]}"
            )

    else:

        st.warning(
            "No meetings scheduled."
        )

except:

    st.warning(
        "No meeting data found."
    )

st.divider()

# ==========================================
# ACTIVE ESCALATIONS
# ==========================================

st.subheader("⚠️ Active Escalations")

try:

    escalations = conn.execute(
        """
        SELECT supplier,
               issue
        FROM escalations
        WHERE status='Open'
        """
    ).fetchall()

    if escalations:

        for esc in escalations:

            st.error(
                f"{esc[0]} - {esc[1]}"
            )

    else:

        st.success(
            "No active escalations."
        )

except:

    st.success(
        "No escalation table found yet."
    )

st.divider()

# ==========================================
# PLATFORM STATUS
# ==========================================

st.subheader("📈 Platform Status")

st.success("✅ Database Connected")

st.success(
    f"✅ {request_count} procurement requests processed"
)

st.success(
    f"✅ {meeting_count} meetings tracked"
)

st.success(
    "✅ Procurement Workflow Active"
)

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.success(
    "🚀 Procurement AI Platform Ready"
)

conn.close()