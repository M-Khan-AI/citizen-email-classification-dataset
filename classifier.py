"""
Email classifier using the Gemini API.

Function:
    classify_email(email_text) -> str

Returns one valid category label or "Uncertain".
"""

import os
import re
import string

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompt import CLASSIFICATION_PROMPT


# ==========================================
# Load environment variables
# ==========================================

load_dotenv()


# ==========================================
# Valid classification labels
# ==========================================

VALID_LABELS = {
    "Schedule Change",
    "Missed Pickup",
    "Complaint",
    "General Info",
    "Uncertain",
}


# ==========================================
# Helpers
# ==========================================

def _normalize(text: str) -> str:
    """Lowercase, strip surrounding whitespace/punctuation, collapse spaces."""
    text = text.strip()
    # Drop wrapping quotes/punctuation Gemini sometimes adds
    # (e.g. '"Missed Pickup."' -> 'Missed Pickup')
    text = text.strip(string.punctuation + " \t\n\r")
    return " ".join(text.split()).casefold()


def _match_label(raw_text: str) -> str:
    """Map raw model output to a valid label, or 'Uncertain' if ambiguous."""
    cleaned = _normalize(raw_text)

    if not cleaned:
        return "Uncertain"

    # 1. Exact match (after normalization) — the common, expected case.
    for label in VALID_LABELS:
        if cleaned == label.casefold():
            return label

    # 2. Whole-phrase match using word boundaries, in case the model added
    #    minor padding (e.g. "Category: Missed Pickup").
    #    Word boundaries prevent one label's text from accidentally being a
    #    substring of a longer, unrelated string.
    matches = [
        label
        for label in VALID_LABELS
        if re.search(r"\b" + re.escape(label.casefold()) + r"\b", cleaned)
    ]

    if len(matches) == 1:
        return matches[0]

    # 0 matches, or more than 1 (genuinely ambiguous) -> Uncertain.
    return "Uncertain"


# ==========================================
# Email classification function
# ==========================================

def classify_email(email_text: str) -> str:
    """
    Classify an email using the Gemini API.

    Args:
        email_text (str): The email body to classify.

    Returns:
        str: A valid category label or "Uncertain".
    """

    # Check for invalid or empty input
    if not isinstance(email_text, str) or not email_text.strip():
        return "Uncertain"

    try:
        # Get Gemini API key
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            print("Error: GEMINI_API_KEY is missing.")
            return "Uncertain"

        # Initialize Gemini client
        client = genai.Client(api_key=api_key)

        # Configure model response.
        # NOTE: gemini-3.6-flash is a "thinking" model — by default it
        # spends part of max_output_tokens on internal reasoning before
        # writing the visible answer. With a tiny token budget this can
        # produce an empty or truncated response (e.g. "Miss" instead of
        # "Missed Pickup"). We set thinking_level to MINIMAL since this
        # is a simple classification task that doesn't need deep
        # reasoning, and give max_output_tokens real headroom so the
        # label always has room to be written out in full.
        config = types.GenerateContentConfig(
            system_instruction=CLASSIFICATION_PROMPT,
            temperature=0.0,
            max_output_tokens=200,
            thinking_config=types.ThinkingConfig(
                thinking_level="MINIMAL",
            ),
        )

        # Send email to Gemini
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
            contents=email_text,
            config=config,
        )

        # Guard against empty/blocked responses before touching .text,
        # since some SDK versions raise instead of returning None when
        # there are no candidates (e.g. safety block, empty finish).
        if not getattr(response, "candidates", None):
            print("Gemini returned no candidates (possibly blocked).")
            return "Uncertain"

        result = response.text

        print("RAW GEMINI RESPONSE:", repr(result))

        if not result:
            return "Uncertain"

        return _match_label(result)

    except Exception as error:
        print(f"Classification API error: {error}")
        return "Uncertain"


# ==========================================
# Run a sample classification
# ==========================================

if __name__ == "__main__":

    example_email = (
        "The garbage truck did not arrive today. "
        "Please collect our waste as soon as possible."
    )

    print("Email:", example_email)

    category = classify_email(example_email)

    print("Category:", category)