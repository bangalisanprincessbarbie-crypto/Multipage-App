import streamlit as st
import pandas as pd

st.set_page_config(page_title="About Me", page_icon="📖", layout="wide")

st.title("📖 About Me")
st.write(
    """
    A little more about who I am, my background, and what drives me.
    *(Replace this content with your own story!)*
    """
)

# ---------- BIO ----------
left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("My Story")
    st.write(
        """
        I'm a student currently exploring the world of **software development**
        and **data science**. I enjoy solving problems with code, learning new
        frameworks, and turning ideas into working applications.

        This portfolio itself — a multipage Streamlit app — is one of the ways
        I practice building real, interactive web tools with Python.
        """
    )

    st.subheader("🎓 Education")
    st.markdown(
        """
        - **B.S. in [Your Course]** — [Your School], *Expected [Year]*
        - Relevant coursework: Data Structures & Algorithms, Web Development,
          Databases, Human-Computer Interaction
        """
    )

    st.subheader("💡 Interests")
    st.markdown(
        """
        - Web & app development
        - Data analysis & visualization
        - UI/UX design
        - Open-source contribution
        """
    )

with right:
    st.subheader("Fast Facts")
    st.markdown(
        """
        - 🌏 Based in **Masbate, Bicol Region, PH**
        - 🗣️ Languages: Filipino, English
        - ☕ Fuel of choice: Coffee
        - 🎯 Currently learning: Streamlit & Cloud Deployment
        """
    )

st.divider()

# ---------- SKILLS ----------
st.subheader("🛠️ Skills")

skills_data = {
    "Skill": ["Python", "HTML/CSS", "SQL", "Data Analysis", "Git/GitHub", "Streamlit"],
    "Proficiency (%)": [85, 70, 65, 75, 80, 78],
}
df_skills = pd.DataFrame(skills_data)

show_chart = st.toggle("Show as chart instead of bars", value=False)

if show_chart:
    st.bar_chart(df_skills.set_index("Skill"))
else:
    for _, row in df_skills.iterrows():
        st.write(f"**{row['Skill']}**")
        st.progress(int(row["Proficiency (%)"]))

st.divider()

# ---------- INTERACTIVE: PERSONALITY QUIZ ----------
st.subheader("🧩 Get to Know My Working Style")
pace = st.select_slider(
    "How do you think I prefer to work?",
    options=["Slow & Careful", "Balanced", "Fast & Iterative"],
    value="Balanced",
)
st.write(f"Your guess: **{pace}** — honestly, that's pretty close! I like to prototype fast, then refine.")

st.caption("Thanks for getting to know me a bit better!")