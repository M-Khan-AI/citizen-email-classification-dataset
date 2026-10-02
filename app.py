import pandas as pd
import streamlit as st
from classifier import classify_email

# 1. Header
st.title("📧 Citizen Email Classifier")
st.write("Classify citizen emails into the appropriate service category.")

# Initialize session state for button persistence
if "show_report" not in st.session_state:
    st.session_state.show_report = False

# 2. Input field
email = st.text_area(
    "Paste citizen email:",
    height=180
)

# 3. Classify action
if st.button("🔍 Classify"):
    if email.strip():
        result = classify_email(email)
        st.success(f"Predicted Category: {result}")
    else:
        st.warning("Please enter an email first.")

st.divider()

# 4. Evaluation Report Button (Toggle state)
if st.button("📊 View Evaluation Report"):
    st.session_state.show_report = not st.session_state.show_report

# 5. Render Evaluation Report directly from evaluation_report.md
if st.session_state.show_report:
    try:
        with open("evaluation_report.md", "r", encoding="utf-8") as f:
            report_content = f.read()

        # Link to report on GitHub (Replace URL with your repo link)
        github_url = "https://github.com/M-Khan-AI/citizen-email-classification-dataset/blob/main/evaluation_report.md"
        st.markdown(f"🔗 **[Open Raw evaluation_report.md on GitHub]({github_url})**")

        # Truncate content right before the 'Uncertain' cases section
        target_section = "Cases Returned as 'Uncertain' by the Model"
        if target_section in report_content:
            report_content = report_content.split(target_section)[0]

        st.markdown(report_content)
    except FileNotFoundError:
        st.error("`evaluation_report.md` not found. Please ensure the file is saved in the same directory as `app.py`.")