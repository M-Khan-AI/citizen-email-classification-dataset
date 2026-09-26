"""
Evaluate classify_email() against a labeled dataset.

Usage:
    python evaluate.py
    python evaluate.py --input emails_labeled.csv --output evaluation_report.md
    python evaluate.py --limit 20        # quick test on first 20 rows

What this script does:
    1. Loads a labeled CSV (columns: email_text, label)
    2. Runs classify_email() on every row (real Gemini API calls)
    3. Applies the keyword-based fallback (fallback.py) to any
       "Uncertain" rows
    4. Hands the results to report.py to compute metrics and write
       the markdown report
"""

import argparse
import sys
import time

import pandas as pd

from classifier import classify_email, VALID_LABELS
from fallback import keyword_fallback
from report import build_report


REAL_LABELS = sorted(VALID_LABELS - {"Uncertain"})


def run_classification(df: pd.DataFrame, limit: int | None, delay: float) -> pd.DataFrame:
    """Run classify_email() on every row and add a predicted_label column."""
    if limit:
        df = df.head(limit).copy()

    predictions = []
    total = len(df)

    for i, row in enumerate(df.itertuples(index=False), start=1):
        pred = classify_email(row.email_text)
        predictions.append(pred)
        print(f"[{i}/{total}] true={row.label!r:16} predicted={pred!r}")
        if delay:
            time.sleep(delay)

    df = df.copy()
    df["predicted_label"] = predictions
    return df


def apply_fallback(df: pd.DataFrame) -> pd.DataFrame:
    """Add a final_label column: predicted_label, with keyword fallback
    applied wherever the model said 'Uncertain'."""
    df = df.copy()
    df["final_label"] = df.apply(
        lambda r: keyword_fallback(r["email_text"])
        if r["predicted_label"] == "Uncertain"
        else r["predicted_label"],
        axis=1,
    )
    return df


def main():
    parser = argparse.ArgumentParser(description="Evaluate classify_email() on a labeled dataset.")
    parser.add_argument("--input", default="emails_labeled.csv", help="Path to labeled CSV")
    parser.add_argument("--output", default="evaluation_report.md", help="Path to write the markdown report")
    parser.add_argument("--limit", type=int, default=None, help="Only evaluate the first N rows (for quick tests)")
    parser.add_argument("--delay", type=float, default=0.0, help="Seconds to sleep between API calls (avoid rate limits)")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.input)
    except FileNotFoundError:
        print(f"Error: could not find {args.input}")
        sys.exit(1)

    if "email_text" not in df.columns or "label" not in df.columns:
        print("Error: CSV must have 'email_text' and 'label' columns.")
        sys.exit(1)

    df = run_classification(df, limit=args.limit, delay=args.delay)
    df = apply_fallback(df)
    build_report(df, args.output, REAL_LABELS)


if __name__ == "__main__":
    main()