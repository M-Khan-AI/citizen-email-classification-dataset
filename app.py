
import streamlit as st
from classifier import classify_email


def normalize_result(result):
    """Extract and normalize the classification label."""

    # Handle tuple or list results, such as ("Uncertain", 0.45)
    if isinstance(result, (tuple, list)):
        if not result:
            return None
        result = result[0]

    if result is None:
        return None

    # Remove whitespace and surrounding quotation marks
    return str(result).strip().strip("\"'").strip()


def is_uncertain(result) -> bool:
    """Return True if the classification is uncertain."""

    result = normalize_result(result)

    if result is None:
        return True

    text = result.casefold()

    return (
        text == ""
        or "uncertain" in text
        or text in {"unknown", "unclassified"}
    )


# 1. Header
st.title("📧 Citizen Email Classifier")
st.write("Classify citizen emails into the appropriate service category.")

# 2. Initialize session state
if "show_report" not in st.session_state:
    st.session_state.show_report = False

# 3. Email input
email = st.text_area(
    "Paste citizen email:",
    height=180
)

# 4. Classify action
if st.button("🔍 Classify"):
    if not email.strip():
        st.warning("Please enter an email first.")
    else:
        try:
            raw_result = classify_email(email)
            result = normalize_result(raw_result)

            # Check for temporary AI/API errors
            if result and any(
                message in result.casefold()
                for message in [
                    "model busy",
                    "please try again",
                    "api error",
                    "rate limit",
                ]
            ):
                st.warning(
                    "⚠️ The AI service is temporarily unavailable. "
                    "Please try again later."
                )

            # Check for uncertain classification
            elif is_uncertain(result):
                st.warning(
                    "⚠️ **Uncertain classification.** "
                    "The model could not confidently assign this email "
                    "to a service category. Please review it manually "
                    "or route it to a human agent."
                )

            # Display a valid category
            else:
                st.success(f"Predicted Category: {result}")

        except Exception:
            st.error(
                "Classification failed. Please try again "
                "or review the email manually."
            )

st.divider()

# 5. Evaluation Report Button
if st.button("📊 View Evaluation Report"):
    st.session_state.show_report = not st.session_state.show_report

# 6. Display Evaluation Report
if st.session_state.show_report:
    try:
        with open("evaluation_report.md", "r", encoding="utf-8") as f:
            report_content = f.read()

        github_url = (
            "https://github.com/M-Khan-AI/"
            "citizen-email-classification-dataset/"
            "blob/main/evaluation_report.md"
        )

        st.markdown(
            f"🔗 **[Open evaluation_report.md on GitHub]({github_url})**"
        )

        # Hide the detailed uncertain-cases section in the app
        target_section = "Cases Returned as 'Uncertain' by the Model"

        if target_section in report_content:
            report_content = report_content.split(target_section, 1)[0]

        st.markdown(report_content)

    except FileNotFoundError:
        st.error(
            "`evaluation_report.md` not found. Please ensure the file "
            "is saved in the same directory as `app.py`."
        )
