# Citizen Email Classification

A small tool that classifies incoming citizen emails about waste collection
into one of four categories using the Gemini API, with an automatic
`Uncertain` fallback when the intent isn't clear.

## Categories

| Label | Meaning |
|---|---|
| `Schedule Change` | Citizen wants to change, request, confirm, or ask about pickup timing |
| `Missed Pickup` | Scheduled collection did not happen |
| `Complaint` | Service issue not primarily a missed pickup or schedule change |
| `General Info` | General question about the service |
| `Uncertain` | Fallback when the email can't be confidently classified |

## Project Structure

```
citizen-email-classification-dataset/
├── classifier.py          # Core classify_email() function — calls Gemini, parses response
├── prompt.py               # System prompt sent to the model
├── evaluate.py              # Runs classify_email() on the labeled dataset (single-command evaluation)
├── fallback.py               # Keyword-based fallback rule for "Uncertain" cases
├── report.py                  # Builds the markdown evaluation report
├── evaluation_report.md        # Generated accuracy/precision/recall report — see below
├── email_validator.py      # (email input validation helper)
├── emails_labeled.csv       # Labeled email dataset (200 emails) used for evaluation
├── tests/
│   └── tests_classifier.py # Pytest suite — mocks the API, no key required to run
├── requirements.txt        # Python dependencies
├── .env                    # GEMINI_API_KEY (not committed — see .gitignore)
├── .gitignore
└── README.md
```

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   GEMINI_MODEL=gemini-3.6-flash
   ```
   Get a key from [Google AI Studio](https://aistudio.google.com/).

## Usage

```python
from classifier import classify_email

result = classify_email(
    "The garbage truck did not arrive today. Please collect our waste."
)
print(result)  # -> "Missed Pickup"
```

Or run the built-in example directly:
```bash
python classifier.py
```

## Testing

Tests run fully mocked — no real API key or network call needed:
```bash
pytest tests/tests_classifier.py -v
```

## Evaluation

`classify_email()` has been evaluated against a labeled dataset of 200
citizen emails (`emails_labeled.csv`), measuring accuracy, precision,
and recall per category, plus the effect of a simple keyword-based
fallback rule for cases the model returns as `"Uncertain"`.

Run the evaluation yourself with a single command:
```bash
python evaluate.py
```

Full results: **[evaluation_report.md](evaluation_report.md)**

Author:
Muhammad Khan