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
├── email_validator.py      # (email input validation helper)
├── emails_labeled.csv       # Sample/labeled email dataset
├── requirements.txt        # Python dependencies
├── .env                    # GEMINI_API_KEY (not committed — see .gitignore)
├── .gitignore
└── README.md
```
## Setup
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
pytest tests/tests_classifier.py -v
```
## Notes
- `gemini-3.6-flash` is a "thinking" model. `classifier.py` sets
  `thinking_level="MINIMAL"` and a generous `max_output_tokens` to avoid
  the model spending its output budget on internal reasoning instead of
  the visible label.
- The email body is always treated as data, not instructions — the prompt
  explicitly tells the model to ignore any embedded commands in the email.