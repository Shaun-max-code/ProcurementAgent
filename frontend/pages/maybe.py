import streamlit as st

from backend.agents.maybe_agent import (
    get_maybe_questions,
    unique_questions
)

st.title("❓ MAYBE Question Aggregator")

questions = unique_questions()

if not questions:

    st.success("No MAYBE questions")

else:

    st.subheader(
        "Questions To Send Client"
    )

    for i, q in enumerate(
        questions,
        start=1
    ):
        answer = st.text_input(
    f"Client Answer {i}"
)

    if answer:

        st.success(
        "Answer Recorded"
    )

        st.warning(
            f"{i}. {q}"
        )