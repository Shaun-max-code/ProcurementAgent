# frontend/pages/followup.py

import streamlit as st

st.title("📝 Follow-Up Generator")

notes = st.text_area("Meeting Notes")

if st.button("Generate Follow-Up"):

    st.success("Follow-Up Created")

    st.write("Summary:")
    st.write("Supplier interested in collaboration.")

    st.write("Next Steps:")
    st.write("- Send samples")
    st.write("- Discuss pricing")