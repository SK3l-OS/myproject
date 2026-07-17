import streamlit as st
import pandas as pd
from pathlib import Path


st.set_page_config(
    page_title="Admin Panel",
    page_icon="🔐"
)


# Login function
def login():

    st.title("🔐 Admin Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    login_button = st.button("Login")


    if login_button:

        if (
            username == st.secrets["ADMIN_USERNAME"]
            and password == st.secrets["ADMIN_PASSWORD"]
        ):

            st.session_state["logged_in"] = True
            st.success("Login successful!")
            st.rerun()

        else:
            st.error("Incorrect username or password")


# Check if logged in
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False



if not st.session_state["logged_in"]:

    login()


else:

    st.title("⚙️ Admin Dashboard")

    st.success("Welcome Admin")

    if st.button("View Password"):
         
         
         st.write(f"🔑 Gmail PW is Bmonth/last2#ofYOB")
         
if st.button("Logout"):

        st.session_state["logged_in"] = False
        st.rerun()