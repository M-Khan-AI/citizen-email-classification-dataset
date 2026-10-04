# Citizen Email Classification

## Project Overview
This project contains a labeled dataset of citizen emails related to CleanCity waste collection services.
The dataset is designed to be used for testing and evaluating an LLM-based email classification system. Each email is manually assigned to one of four categories:

## Categories

System receives citizen emails and classifies them into categories such as:

| Label | Meaning |
|---|---|
| `Schedule Change` | Citizen wants to change, request, confirm, or ask about pickup timing |
| `Missed Pickup` | Scheduled collection did not happen |
| `Complaint` | Service issue not primarily a missed pickup or schedule change |
| `General Info` | General question about the service |
| `Uncertain` | Fallback when the email can't be confidently classified |

## Project goal

The goal of this project is to automatically categorize citizen emails for CleanCity Services, helping staff process incoming waste-service requests more efficiently.

## Main features

LLM-based email classification
Four email categories
Fallback keyword classification
API error handling
Evaluation using accuracy, precision, and recall
Unit tests
Interactive dashboard, if you implemented one

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
├── README.md
├── HANDOVER.md
└── LICENSE.md
```
## Setup

Installation

Clone repository
git clone <your-github-repository-url>
cd clean-city-email-classifier
Create virtual environment
python -m venv .venv
Activate it on Windows
.venv\Scripts\activate
Install dependencies
pip install -r requirements.txt

## Api Kye steup   

1. Get a Gemini API key from Google AI Studio.
2. Create a `.env` file in the project root.
3. Add `GEMINI_API_KEY=your_api_key_here` to the `.env` file.
4. Install dependencies using `pip install -r requirements.txt`.
5. Never upload your `.env` file or API key to GitHub.

## Usage

python classifier.py

explain what the user should expect.

You might show:

Input:
"Our garbage was not collected yesterday."

Output:
Missed Pickup

If you have an evaluation script:

python evaluate.py

explain:

This command runs the classifier on the 200-email dataset and calculates accuracy, precision, and recall.

If you have a Streamlit dashboard:

streamlit run app.py

explain that this starts the web interface.

If you have tests:

pytest

explain that this runs the automated tests.

## Troubleshooting

It means you should document common problems and their solutions.

For example:

API key error

Problem:

API key not found

Solution:

Check that your .env file exists and contains:

GEMINI_API_KEY=your_api_key_here
Missing package

Problem:

ModuleNotFoundError

Solution:

Make sure your virtual environment is activated and run:

pip install -r requirements.txt
Streamlit doesn't start

Problem:

'streamlit' is not recognized

Solution:

Run:

pip install streamlit

Then:

streamlit run app.py
Tests fail

Problem:

pytest: command not found

Solution:

pip install pytest

Then:

pytest
















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
## Click the following link to go evaluation_report.md


: **[evaluation_report.md](evaluation_report.md)**


No personally identifiable information or real private customer conversations were included.

## 📧 Citizen Email Classifier & Dashboard

An interactive Streamlit web application that uses the Google Gemini API to classify citizen service emails into standardized categories and present detailed model performance reports.

## 🚀 Features

-Automated Email Classification:** Paste any citizen inquiry to instantly classify it into service categories (*Schedule Change*, *Missed Pickup*, *Complaint*, *General Info*, or *Uncertain*).
-  Interactive Evaluation Report:** Toggle the model performance report directly inside the Streamlit UI.
- Direct Link & Access:** Access the raw `evaluation_report.md` file directly via the UI or GitHub repository link.

--- 

## 🛠️ Tech Stack

- **Frontend / UI:** Streamlit
- **Backend / AI:** Python, Google Gemini API (`google-genai`)
- **Environment Management:** `python-dotenv`
---

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author 
Muhammad Khan
