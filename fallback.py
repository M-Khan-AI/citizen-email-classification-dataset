"""
Simple rule-based fallback classifier.

Used when classify_email() (the LLM-based classifier in classifier.py)
returns "Uncertain". This is NOT meant to replace the model — it's a
lightweight safety net that checks the email text for a handful of
high-signal keywords/phrases per category. If nothing matches, the
email stays "Uncertain".
"""

FALLBACK_KEYWORDS = {
    "Missed Pickup": [
        "did not come", "didn't come", "did not arrive", "not collected",
        "not been collected", "missed pickup", "missed collection",
        "skipped", "without emptying", "still full", "truck did not",
    ],
    "Schedule Change": [
        "timetable", "reschedule", "rescheduled", "alternative collection",
        "public holiday", "collection date", "collection schedule",
        "move because", "usual collection day", "collection day",
    ],
    "Complaint": [
        "complain", "complaint", "unhappy", "overflowing", "smell",
        "damaged", "broken", "hazard", "blocked", "torn bags",
        "scattered rubbish", "flies",
    ],
    "General Info": [
        "opening hours", "what materials", "how do i", "recycling centre",
        "bulky-waste", "compost", "how to report", "request an extra",
        "sorting household waste", "moving into the area",
    ],
}


def keyword_fallback(email_text: str) -> str:
    """
    Very simple rule-based classifier used only as a fallback for
    emails the LLM returned 'Uncertain' for.

    Args:
        email_text (str): The email body to check.

    Returns:
        str: A valid category label if a keyword match is found,
             otherwise "Uncertain" unchanged.
    """
    if not isinstance(email_text, str) or not email_text.strip():
        return "Uncertain"

    text = email_text.lower()

    for label, keywords in FALLBACK_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return label

    return "Uncertain"


if __name__ == "__main__":
    examples = [
        "The truck did not come today.",
        "Has the timetable changed?",
        "The bin is overflowing and smells.",
        "What materials are accepted, opening hours?",
        "asdkjh random gibberish with no keywords",
    ]
    for email in examples:
        print(f"{keyword_fallback(email):16} <- {email}")