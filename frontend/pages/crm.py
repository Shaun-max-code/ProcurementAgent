import streamlit as st
import sqlite3
import pandas as pd

DB = "procurement.db"

st.set_page_config(
    page_title="CRM Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Supplier CRM Dashboard")

conn = sqlite3.connect(DB)

# ==========================================
# KPI COUNTERS
# ==========================================

try:
    yes_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM supplier_responses
        WHERE response='YES'
        """
    ).fetchone()[0]
except:
    yes_count = 0

try:
    no_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM supplier_responses
        WHERE response='NO'
        """
    ).fetchone()[0]
except:
    no_count = 0

try:
    maybe_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM supplier_responses
        WHERE response='MAYBE'
        """
    ).fetchone()[0]
except:
    maybe_count = 0

try:
    handoff_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM human_handoffs
        """
    ).fetchone()[0]
except:
    handoff_count = 0

try:
    meeting_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM meetings
        """
    ).fetchone()[0]
except:
    meeting_count = 0

try:
    escalation_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM escalations
        """
    ).fetchone()[0]
except:
    escalation_count = 0

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "✅ YES Responses",
        yes_count
    )

with col2:
    st.metric(
        "❌ NO Responses",
        no_count
    )

with col3:
    st.metric(
        "❓ MAYBE Responses",
        maybe_count
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🤝 Human Handoffs",
        handoff_count
    )

with col2:
    st.metric(
        "📅 Meetings",
        meeting_count
    )

with col3:
    st.metric(
        "⚠️ Escalations",
        escalation_count
    )

st.divider()

# ==========================================
# PIPELINE STATUS
# ==========================================

st.subheader("🔄 Supplier Pipeline")

try:

    pipeline = pd.read_sql_query(
        """
        SELECT
            supplier,
            response,
            status,
            response_date
        FROM supplier_responses
        ORDER BY id DESC
        """,
        conn
    )

    if not pipeline.empty:

        st.dataframe(
            pipeline,
            use_container_width=True
        )

    else:

        st.warning(
            "No supplier activity found."
        )

except Exception as e:

    st.error(e)

st.divider()

# ==========================================
# HUMAN HANDOFFS
# ==========================================

st.subheader("🤝 Human Handoff Queue")

try:

    handoffs = pd.read_sql_query(
        """
        SELECT *
        FROM human_handoffs
        ORDER BY id DESC
        """,
        conn
    )

    if not handoffs.empty:

        st.dataframe(
            handoffs,
            use_container_width=True
        )

    else:

        st.info(
            "No handoffs yet."
        )

except:

    st.info(
        "Human handoff table not found."
    )

st.divider()

# ==========================================
# ACTIVE ESCALATIONS
# ==========================================

st.subheader("⚠️ Active Escalations")

try:

    escalations = pd.read_sql_query(
        """
        SELECT *
        FROM escalations
        ORDER BY id DESC
        """,
        conn
    )

    if not escalations.empty:

        st.dataframe(
            escalations,
            use_container_width=True
        )

    else:

        st.success(
            "No escalations."
        )

except:

    st.success(
        "No escalations."
    )

st.divider()

# ==========================================
# RECENT MEETINGS
# ==========================================

st.subheader("📅 Recent Meetings")

try:

    meetings = pd.read_sql_query(
        """
        SELECT *
        FROM meetings
        ORDER BY id DESC
        LIMIT 10
        """,
        conn
    )

    if not meetings.empty:

        st.dataframe(
            meetings,
            use_container_width=True
        )

    else:

        st.info(
            "No meetings scheduled."
        )

except:

    st.info(
        "No meeting data."
    )

conn.close()