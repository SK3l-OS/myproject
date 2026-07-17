from pathlib import Path

import toml
import streamlit as st

CONFIG = toml.load("config.toml")

st.set_page_config(
    page_title=CONFIG["site"]["name"],
    page_icon="💻",
    layout="wide",
)

theme = CONFIG["theme"]

st.markdown(
    f"""
<style>
.stApp {{
    background-color: {theme["backgroundColor"]};
    color: {theme["textColor"]};
}}

.card {{
    padding:20px;
    border-radius:15px;
    background:#1f2937;
    border:1px solid #333;
}}

a {{
    text-decoration:none;
}}
</style>
""",
    unsafe_allow_html=True,
)

st.title(CONFIG["site"]["name"])
st.subheader(CONFIG["site"]["title"])

st.write(CONFIG["site"]["description"])

left, right = st.columns([2, 1])

with left:

    st.header("About Me")

    st.write("""
Welcome to my portfolio.

This website showcases my projects, programming skills,
cybersecurity experience, and ways to contact me.
""")

    st.header("Skills")

    skills = [
        "Python",
        "Flask",
        "Streamlit",
        "Cybersecurity",
        "Linux",
        "Networking",
        "Git",
    ]

    cols = st.columns(4)

    for i, skill in enumerate(skills):
        cols[i % 4].success(skill)

with right:

    image = Path("assets/profile.jpg")

    if image.exists():
        st.image(str(image), use_container_width=True)

    st.markdown("### Contact")

    st.write(f"🕊️ {CONFIG['social']['email']}")
    st.write(f"🦊 {CONFIG['social']['github']}")

st.divider()

st.header("Featured Projects")

projects = [
    {
        "title": "Cyber Dashboard",
        "desc": "A dashboard for monitoring cybersecurity events.",
        "tech": "Python, Streamlit",
    },
    {
        "title": "Portfolio Website",
        "desc": "Responsive personal portfolio.",
        "tech": "Python",
    },
    {
        "title": "Automation Scripts",
        "desc": "Python tools for automation.",
        "tech": "Python",
    },
]

for project in projects:
    st.markdown(
        f"""
<div class="card">
<h3>{project['title']}</h3>
<p>{project['desc']}</p>
<b>{project['tech']}</b>
</div>
<br>
""",
        unsafe_allow_html=True,
    )

resume = Path("assets/resume.pdf")

if resume.exists():
    with open(resume, "rb") as pdf:
        st.download_button(
            "📄 Download Resume",
            pdf,
            file_name="Resume.pdf",
            mime="application/pdf",
        )