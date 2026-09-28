# Citizen Email Classification

## Project Overview
This project contains a labeled dataset of citizen emails related to CleanCity waste collection services.
The dataset is designed to be used for testing and evaluating an LLM-based email classification system. Each email is manually assigned to one of four categories:

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

<<<<<<< HEAD
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

## Api Kye steup   

1. Get a Gemini API key from Google AI Studio.
2. Create a `.env` file in the project root.
3. Add `GEMINI_API_KEY=your_api_key_here` to the `.env` file.
4. Install dependencies using `pip install -r requirements.txt`.
5. Never upload your `.env` file or API key to GitHub.


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
## Link will lead to evaluation_report.md

: **[evaluation_report.md](evaluation_report.md)**

## Author:
Muhammad Khan

No personally identifiable information or real private customer conversations were included.

## What Was Difficult:

The main challenge was creating enough realistic and varied emails while keeping the four category labels consistent. Some messages could potentially fit more than one category, so each email was reviewed based on its primary purpose and assigned to the most appropriate predefined category.

## What Was Left Out
This task focuses only on creating and labeling the dataset. The LLM classification system, model evaluation, and automated email processing are not included in this dataset creation stage.
