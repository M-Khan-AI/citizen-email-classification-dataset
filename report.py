"""
Build a markdown evaluation report from classification results.

Takes a DataFrame with columns: email_text, label, predicted_label,
final_label (produced by evaluate.py) and writes a markdown report
summarizing accuracy, per-category precision/recall/F1, Uncertain
cases, fallback effectiveness, and a confusion matrix.
"""

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def build_report(df: pd.DataFrame, output_path: str, real_labels: list[str]) -> None:
    """
    Write a markdown evaluation report to output_path.

    Args:
        df: DataFrame with columns email_text, label, predicted_label,
            final_label.
        output_path: Path to write the .md report to.
        real_labels: The valid category labels, excluding "Uncertain"
            (used to build per-category metric tables in a fixed order).
    """
    y_true = df["label"]
    y_pred_model = df["predicted_label"]
    y_pred_final = df["final_label"]

    acc_model = accuracy_score(y_true, y_pred_model)
    acc_final = accuracy_score(y_true, y_pred_final)

    report_model = classification_report(
        y_true, y_pred_model, labels=real_labels, output_dict=True, zero_division=0
    )
    report_final = classification_report(
        y_true, y_pred_final, labels=real_labels, output_dict=True, zero_division=0
    )

    uncertain_rows = df[df["predicted_label"] == "Uncertain"]
    still_uncertain_rows = df[df["final_label"] == "Uncertain"]

    lines = []
    lines.append("# Email Classification – Evaluation Report\n")
    lines.append(f"Dataset size: **{len(df)}** labeled emails\n")

    # --- Overall accuracy ---
    lines.append("## Overall Accuracy\n")
    lines.append("| Stage | Accuracy |")
    lines.append("|---|---|")
    lines.append(f"| Model only (raw `classify_email()` output) | {acc_model:.1%} |")
    lines.append(f"| Model + keyword fallback | {acc_final:.1%} |")
    lines.append("")
    threshold_note = (
        "✅ Meets the 70% accuracy target."
        if acc_model >= 0.70
        else "⚠️ Below the 70% target — see notes below."
    )
    lines.append(f"{threshold_note}\n")

    # --- Per-category metrics (model only) ---
    lines.append("## Per-Category Metrics (model only, before fallback)\n")
    lines.append("| Category | Precision | Recall | F1 | Support |")
    lines.append("|---|---|---|---|---|")
    for label in real_labels:
        m = report_model[label]
        lines.append(
            f"| {label} | {m['precision']:.2f} | {m['recall']:.2f} "
            f"| {m['f1-score']:.2f} | {int(m['support'])} |"
        )
    lines.append("")

    # --- Per-category metrics (after fallback) ---
    lines.append("## Per-Category Metrics (after keyword fallback)\n")
    lines.append("| Category | Precision | Recall | F1 | Support |")
    lines.append("|---|---|---|---|---|")
    for label in real_labels:
        m = report_final[label]
        lines.append(
            f"| {label} | {m['precision']:.2f} | {m['recall']:.2f} "
            f"| {m['f1-score']:.2f} | {int(m['support'])} |"
        )
    lines.append("")

    # --- Uncertain cases ---
    lines.append("## Cases Returned as 'Uncertain' by the Model\n")
    lines.append(f"Total: **{len(uncertain_rows)}** out of {len(df)} emails.\n")
    if len(uncertain_rows) > 0:
        lines.append("| True Label | Email (truncated) |")
        lines.append("|---|---|")
        for _, row in uncertain_rows.iterrows():
            snippet = row["email_text"][:100].replace("\n", " ").replace("|", "/")
            lines.append(f"| {row['label']} | {snippet}... |")
        lines.append("")
    else:
        lines.append("None — the model returned a real label for every email.\n")

    # --- Fallback logic explanation ---
    lines.append("## Fallback Logic\n")
    lines.append(
        "When `classify_email()` returns `\"Uncertain\"`, a simple "
        "keyword-matching function (`keyword_fallback()` in `fallback.py`) "
        "is applied as a second pass. It checks the email text (lowercased) "
        "against a short list of high-signal phrases per category — for "
        "example, `\"did not come\"` or `\"missed pickup\"` → **Missed "
        "Pickup**; `\"overflowing\"` or `\"smell\"` → **Complaint**; "
        "`\"opening hours\"` or `\"how do i\"` → **General Info**; "
        "`\"timetable\"` or `\"reschedule\"` → **Schedule Change**. "
        "The first matching category wins. If no keyword matches, the "
        "email stays `\"Uncertain\"`.\n"
    )
    lines.append(
        f"This fallback resolved **{len(uncertain_rows) - len(still_uncertain_rows)}** "
        f"of the **{len(uncertain_rows)}** Uncertain cases; "
        f"**{len(still_uncertain_rows)}** remained Uncertain after the fallback.\n"
    )

    # --- Confusion matrix (model only) ---
    all_labels_seen = sorted(set(y_true) | set(y_pred_model))
    cm = confusion_matrix(y_true, y_pred_model, labels=all_labels_seen)
    lines.append("## Confusion Matrix (model only)\n")
    header = "| True \\ Predicted | " + " | ".join(all_labels_seen) + " |"
    lines.append(header)
    lines.append("|" + "---|" * (len(all_labels_seen) + 1))
    for i, label in enumerate(all_labels_seen):
        row_vals = " | ".join(str(v) for v in cm[i])
        lines.append(f"| {label} | {row_vals} |")
    lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\nReport written to: {output_path}")
    print(f"Model-only accuracy: {acc_model:.1%}")
    print(f"With fallback accuracy: {acc_final:.1%}")