import streamlit as st

st.title("Projects")

projects = [
    (
        "Cyber Dashboard",
        "Security monitoring dashboard."
    ),
    (
        "Portfolio Website",
        "Built using Streamlit."
    ),
    (
        "Python Automation",
        "Automation tools and utilities."
    ),
]

for title, desc in projects:
    with st.expander(title):
        st.write(desc)