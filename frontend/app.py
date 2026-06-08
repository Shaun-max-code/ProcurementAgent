import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Procurement AI",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("🚀 Procurement AI Platform")

st.markdown("""
### Intelligent Supplier Discovery & Procurement Workflow

Manage your entire procurement process:

- 📋 Client Intake
- 🏭 Supplier Matching
- 📅 Meeting Coordination
- 📝 Follow-Ups
- ⚠ Escalations

Use the sidebar to navigate through the platform.
""")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Brands", "12")

with col2:
    st.metric("Suppliers", "35")

with col3:
    st.metric("Meetings", "7")

with col4:
    st.metric("Escalations", "2")

st.divider()

# Workflow Section
st.subheader("🔄 Procurement Workflow")

st.code("""
Client Intake
      ↓
Supplier Matching
      ↓
Meeting Coordination
      ↓
Follow-Up Generation
      ↓
Escalation Monitoring
""", language="text")

st.divider()

# Platform Overview
st.subheader("📈 Platform Overview")

st.info(
    """
    This platform helps brands discover suppliers,
    coordinate meetings, generate follow-ups,
    and monitor procurement workflows efficiently.
    """
)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)