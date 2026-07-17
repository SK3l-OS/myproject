import streamlit as st

st.title("Contact")

with st.form("contact"):

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")

if submitted:
    st.success(
        "Thank you! This demo does not send emails yet, but it will in the future. For now, you can reach me at edwardsalex4@outlook.com or edwardsalex0001@gmail.com"
    )