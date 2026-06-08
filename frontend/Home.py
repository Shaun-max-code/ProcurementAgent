import streamlit as st

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
automated supplier matching, meeting coordination, follow-up generation,
and escalation monitoring.

---
""")

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🏢 Active Brands",
        "12",
        "+2"
    )

with col2:
    st.metric(
        "🏭 Suppliers",
        "35",
        "+5"
    )

with col3:
    st.metric(
        "📅 Meetings",
        "7",
        "+1"
    )

with col4:
    st.metric(
        "⚠️ Escalations",
        "2",
        "-1"
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
# WORKFLOW
# ==========================================

st.subheader("🔄 Procurement Workflow")

workflow_html = """
<div style="
padding:25px;
border-radius:15px;
background:#1E293B;
font-size:20px;
font-weight:bold;
text-align:center;
line-height:2.2;
">

📋 Client Intake
<br>⬇️<br>

🏭 Supplier Matching
<br>⬇️<br>

📅 Meeting Coordination
<br>⬇️<br>

✉️ Follow-Up Generation
<br>⬇️<br>

⚠️ Escalation Monitoring

</div>
"""

st.markdown(
    workflow_html,
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# FEATURES
# ==========================================

st.subheader("✨ Platform Features")

left, right = st.columns(2)

with left:

    st.info("""
### 📋 Client Intake

Capture procurement requirements:

- Product Name
- Category
- MOQ
- Country
- Client Details
""")

    st.info("""
### 🏭 Supplier Matching

Automatically match suppliers based on:

- Category
- MOQ
- Location
- Procurement Rules
""")

with right:

    st.info("""
### 📅 Meeting Coordination

Generate supplier meeting requests and schedules automatically.
""")

    st.info("""
### ✉️ Follow-Up & Escalation

Track supplier responses and create follow-ups and escalations.
""")

st.divider()

# ==========================================
# PLATFORM STATUS
# ==========================================

st.subheader("📈 Platform Status")

status1, status2, status3 = st.columns(3)

with status1:
    st.success("✅ Intake Agent Online")

with status2:
    st.success("✅ Matching Agent Online")

with status3:
    st.success("✅ Meeting Agent Online")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.success(
    "🚀 Procurement AI Platform Ready. Use the sidebar or Quick Access section to begin."
)