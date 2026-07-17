import streamlit as st
import pandas as pd
import json
from pathlib import Path


st.set_page_config(
    page_title="Admin Panel",
    page_icon="🔐",
    layout="wide"
)


# -----------------------------
# LOAD ADMIN LOGIN SAFELY
# -----------------------------

def get_secret(key, default=None):
    try:
        return st.secrets[key]
    except Exception:
        return default


ADMIN_USERNAME = get_secret(
    "ADMIN_USERNAME",
    "admin"
)

ADMIN_PASSWORD = get_secret(
    "ADMIN_PASSWORD",
    "changeme"
)


# -----------------------------
# LOGIN FUNCTION
# -----------------------------

def login():

    st.title("🔐 Admin Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if (
            username == ADMIN_USERNAME
            and password == ADMIN_PASSWORD
        ):

            st.session_state.logged_in = True
            st.success("Login successful!")

            st.rerun()

        else:

            st.error(
                "Incorrect username or password"
            )


# -----------------------------
# SESSION CHECK
# -----------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



if not st.session_state.logged_in:

    login()
    st.stop()



# -----------------------------
# ADMIN DASHBOARD
# -----------------------------

st.title("⚙️ Owner Dashboard")

st.success(
    "You are logged in as the owner."
)



# -----------------------------
# WEBSITE STATS
# -----------------------------

st.header("📊 Website Statistics")


stats_file = Path(
    "data/stats.json"
)


if stats_file.exists():

    stats = json.loads(
        stats_file.read_text()
    )

else:

    stats = {
        "visits": 0,
        "messages": 0,
        "projects": 0
    }



col1, col2, col3 = st.columns(3)


col1.metric(
    "Visitors",
    stats.get("visits", 0)
)


col2.metric(
    "Messages",
    stats.get("messages", 0)
)


col3.metric(
    "Projects",
    stats.get("projects", 0)
)


# -----------------------------
# PROJECT MANAGEMENT
# -----------------------------

st.header("🚀 Add Project")


project_file = Path(
    "data/projects.json"
)


project_file.parent.mkdir(
    exist_ok=True
)



if project_file.exists():

    projects = json.loads(
        project_file.read_text()
    )

else:

    projects = []



with st.form(
    "add_project"
):

    title = st.text_input(
        "Project Name"
    )

    description = st.text_area(
        "Description"
    )

    tech = st.text_input(
        "Technology Used"
    )


    submit = st.form_submit_button(
        "Add Project"
    )


    if submit:

        projects.append(
            {
                "title": title,
                "description": description,
                "tech": tech
            }
        )


        project_file.write_text(
            json.dumps(
                projects,
                indent=4
            )
        )


        st.success(
            "Project added!"
        )



# -----------------------------
# SHOW PROJECTS
# -----------------------------

st.header("Current Projects")


for project in projects:

    with st.expander(
        project["title"]
    ):

        st.write(
            project["description"]
        )

        st.caption(
            project["tech"]
        )



# -----------------------------
# LOGOUT
# -----------------------------

st.divider()


if st.button(
    "Logout"
):

    st.session_state.logged_in = False

    st.rerun()