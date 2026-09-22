import streamlit as st

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🏠",
    layout="wide",
)

# ---------- EDIT THESE WITH YOUR OWN INFO ----------
FULL_NAME = "Nore May G. Bangalisan"
TAGLINE = "Aspiring Software Developer"
LOCATION = "Milagros, Masbate, Bicol Region, Philippines"

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown(f"### {FULL_NAME}")
    st.write(LOCATION)

# ---------- HEADER ----------
st.title(f"Hi, I'm {FULL_NAME} 👋")
st.subheader(TAGLINE)

st.write(
    "Welcome to my portfolio! This site was built for my "
    "Streamlit Multipage Web Application activity."
)

st.divider()

# ---------- SIMPLE STATS ----------
col1, col3 = st.columns(2)
col1.metric("Projects", "2")
col3.metric("Favorite Language", "Python")

st.divider()

# ---------- ONE SIMPLE INTERACTION ----------
name_input = st.text_input("What's your name?")

if name_input:
    st.write(f"Nice to meet you, {name_input}! 🎉")