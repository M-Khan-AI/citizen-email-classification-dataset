
import csv
from pathlib import Path
from collections import Counter

# ==========================================
# Configuration
# ==========================================

CSV_FILE = Path(__file__).parent / "emails_labeled.csv"

REQUIRED_COLUMNS = ["email_text", "label"]

VALID_LABELS = {
    "Schedule Change",
    "Missed Pickup",
    "Complaint",
    "General Info",
    "schedule_change",
    "missed_pickup",
    "complaint",
    "general_info",
}

MINIMUM_ROWS = 200


# ==========================================
# Email Dataset Validator
# ==========================================

def validate_csv():

    if not CSV_FILE.exists():
        print(f"ERROR: CSV file not found: {CSV_FILE}")
        return

    errors = []
    label_counts = Counter()
    total_rows = 0

    try:
        with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:

            reader = csv.DictReader(file)

            # Check column names
            if reader.fieldnames != REQUIRED_COLUMNS:
                print("ERROR: Incorrect CSV columns.")
                print("Expected:", REQUIRED_COLUMNS)
                print("Found:", reader.fieldnames)
                return

            # Check every row
            for row_number, row in enumerate(reader, start=2):

                total_rows += 1

                # Check for missing or extra columns
                if None in row or any(
                    value is None for value in row.values()
                ):
                    errors.append(
                        f"Row {row_number}: Incorrect number of columns."
                    )
                    continue

                email_text = row["email_text"].strip()
                label = row["label"].strip()

                # Check empty email text
                if not email_text:
                    errors.append(
                        f"Row {row_number}: Email text is empty."
                    )

                # Check empty label
                if not label:
                    errors.append(
                        f"Row {row_number}: Label is empty."
                    )
                    continue

                # Check valid label
                if label not in VALID_LABELS:
                    errors.append(
                        f"Row {row_number}: Invalid label '{label}'."
                    )
                else:
                    label_counts[label] += 1

        # ==========================================
        # Display Validation Results
        # ==========================================

        print("\n========== CSV VALIDATION REPORT ==========")

        print(f"Total email rows: {total_rows}")
        print(f"Required minimum: {MINIMUM_ROWS}")

        if total_rows < MINIMUM_ROWS:
            errors.append(
                f"Dataset contains only {total_rows} rows. "
                f"At least {MINIMUM_ROWS} are required."
            )

        print("\nLabel counts:")

        for label, count in sorted(label_counts.items()):
            print(f"{label}: {count}")

        print("\nValidation errors:")

        if errors:
            for error in errors:
                print("-", error)

            print(f"\nVALIDATION FAILED: {len(errors)} error(s) found.")

        else:
            print("No errors found.")
            print("VALIDATION SUCCESSFUL!")
            print("Your CSV meets the basic dataset requirements.")

    except (OSError, csv.Error) as error:
        print(f"ERROR: Could not read the CSV file: {error}")


# ==========================================
# Run Validator
# ==========================================

if __name__ == "__main__":
    validate_csv()