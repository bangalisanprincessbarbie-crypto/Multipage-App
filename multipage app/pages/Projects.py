import streamlit as st

st.set_page_config(page_title="Projects", page_icon="💼", layout="wide")

st.title("My Projects")
st.write("A few things I've built. Replace these with your own real projects!")

# ---------- EDIT THIS LIST WITH YOUR OWN PROJECTS ----------
projects = [
    {
        "title": "Sales Dashboard",
        "description": "An interactive dashboard to visualize monthly sales trends.",
        "link": "https://github.com/your-username/sales-dashboard",
    },
    {
        "title": "To-Do List Web App",
        "description": "A simple task manager with add, edit, and delete features.",
        "link": "https://github.com/your-username/todo-app",
    },
    {
        "title": "Number Guessing Game",
        "description": "A beginner console game where you guess a random number.",
        "link": "https://github.com/your-username/guessing-game",
    },
    {
        "title": "Weather App",
        "description": "Shows live weather data fetched from an API.",
        "link": "https://github.com/your-username/weather-app",
    },
]

# ---------- SIMPLE SEARCH ----------
search_term = st.text_input("Search projects")

if search_term:
    projects = [p for p in projects if search_term.lower() in p["title"].lower()]

st.divider()

# ---------- SHOW EACH PROJECT ----------
for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.link_button("View on GitHub", project["link"])
    st.divider()