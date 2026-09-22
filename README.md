# Multipage-App
# 🌐 My Streamlit Portfolio — Multipage Web App

A personal portfolio website built with [Streamlit](https://streamlit.io), created for
**Activity 02: Streamlit Multipage App**. It showcases who I am, my skills, my projects,
and how to get in touch — with interactive elements throughout.

## 🗂️ Project Structure

```
streamlit-portfolio/
├── app.py                      # Home page (entry point)
├── pages/
│   ├── 1_📖_About.py           # About Me page
│   ├── 2_💼_Projects.py        # Projects showcase page
│   └── 3_📬_Contact.py         # Contact form page
├── .streamlit/
│   └── config.toml             # Theme configuration
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md
```

Streamlit automatically turns every file inside `pages/` into a separate page in the
sidebar navigation menu — no extra routing code needed. The number prefixes control
page order, and the emojis become the page icons.

## ✨ Features

- **Home** — intro, quick stats, and an interactive "what brings you here" selector
- **About** — bio, education, skills bars/chart toggle, and a working-style slider
- **Projects** — filterable/searchable project cards by category and keyword
- **Contact** — a working input form (demo) with validation and status feedback

## 🚀 Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/streamlit-portfolio.git
   cd streamlit-portfolio
   ```
2. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # on Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```
5. Open the local URL Streamlit prints (usually `http://localhost:8501`).

## 🎨 Personalizing This Template

Before submitting, replace the placeholder content with your own:

| File | What to change |
|---|---|
| `app.py` | `FULL_NAME`, `TAGLINE`, `LOCATION`, `PROFILE_IMAGE_URL`, resume/GitHub/LinkedIn links |
| `pages/1_📖_About.py` | Bio, education, interests, skills list and proficiency levels |
| `pages/2_💼_Projects.py` | The `projects` list — swap in your real projects, links, and tags |
| `pages/3_📬_Contact.py` | Your email, LinkedIn, GitHub, and (optionally) wire the form to a real email service like [Formspree](https://formspree.io) or [EmailJS](https://www.emailjs.com/) |
| `.streamlit/config.toml` | Theme colors, if you want a different look |

## ☁️ Deploying to Streamlit Community Cloud

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Streamlit multipage portfolio"
   git branch -M main
   git remote add origin https://github.com/your-username/streamlit-portfolio.git
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
3. Click **"New app"**.
4. Select this repository, the `main` branch, and set the main file path to `app.py`.
5. Click **"Deploy"**. Streamlit Cloud will install `requirements.txt` automatically and
   give you a public URL like:
   `https://your-app-name.streamlit.app`

## 📤 Submission Checklist

- [ ] GitHub repository link (with all source files + this README)
- [ ] Live Streamlit app link (`https://your-app-name.streamlit.app`)
- [ ] All placeholder content replaced with your own information
- [ ] App tested locally and confirmed working before deployment

---
Built with ❤️ using Python & Streamlit.
