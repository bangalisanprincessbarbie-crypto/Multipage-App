import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")

st.title("📬 Get In Touch")
st.write("I'd love to hear from you! Fill out the form below or reach me through any of the links.")

left, right = st.columns([1.3, 1], gap="large")

# ---------- CONTACT FORM ----------
with left:
    st.subheader("Send Me a Message")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name *")
        email = st.text_input("Your Email *")
        subject = st.selectbox(
            "Subject",
            ["General Inquiry", "Job Opportunity", "Collaboration", "Feedback", "Other"],
        )
        message = st.text_area("Message *", height=150)
        submitted = st.form_submit_button("Send Message", use_container_width=True)

        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all required fields (marked with *).")
            else:
                st.success(f"Thanks, {name}! Your message about '{subject}' has been received. 🎉")
                st.balloons()

st.divider()
st.caption("Thank you for visiting my portfolio — talk soon!")