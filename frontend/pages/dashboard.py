import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Procurement Dashboard")
st.markdown("Welcome to the Procurement AI Platform")

# =====================
# KPI CARDS
# =====================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
        padding:20px;
        border-radius:15px;
        background:#1E293B;
        text-align:center;
    ">
        <h4>🏢 Brands</h4>
        <h1>12</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        padding:20px;
        border-radius:15px;
        background:#1E293B;
        text-align:center;
    ">
        <h4>🏭 Suppliers</h4>
        <h1>35</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        padding:20px;
        border-radius:15px;
        background:#1E293B;
        text-align:center;
    ">
        <h4>📅 Meetings</h4>
        <h1>7</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
        padding:20px;
        border-radius:15px;
        background:#1E293B;
        text-align:center;
    ">
        <h4>⚠ Escalations</h4>
        <h1>2</h1>
    </div>
    """, unsafe_allow_html=True)
st.divider()

# =====================
# WORKFLOW STATUS
# =====================

st.subheader("🔄 Workflow Status")

workflow_data = pd.DataFrame({
    "Stage": [
        "Client Intake",
        "Supplier Matching",
        "Meeting Coordination",
        "Follow-Up",
        "Escalation Monitoring"
    ],
    "Requests": [15, 12, 8, 6, 2]
})

st.dataframe(
    workflow_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================
# RECENT ACTIVITY
# =====================

st.subheader("📌 Recent Activity")

st.success("Protein Bar request submitted")
st.info("Supplier match generated for Cosmetics project")
st.warning("Follow-up pending for FreshFactory")
st.error("Supplier XYZ has not responded in 5 days")

st.divider()

# =====================
# TOP SUPPLIERS
# =====================

st.subheader("🏭 Top Suppliers")

supplier_data = pd.DataFrame({
    "Supplier": [
        "FoodCorp",
        "FreshFactory",
        "NutriFoods",
        "BeautyLabs"
    ],
    "Match Rate": [
        "95%",
        "92%",
        "88%",
        "85%"
    ]
})

st.dataframe(
    supplier_data,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================
# SYSTEM STATUS
# =====================

st.subheader("⚙️ System Status")

st.success("✅ Procurement AI Platform Online")