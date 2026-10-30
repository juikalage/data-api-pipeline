"""Read a CSV file, validate each row, and store the valid ones."""

import csv

from src.storage import init_db, save_rows
from src.validate import validate_row


def run_pipeline(csv_path: str, db_path: str) -> dict:
    """Load a CSV, store valid rows, and return the accepted count and rejected rows."""
    good_rows = []
    rejected = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        for line_no, row in enumerate(csv.DictReader(f), start=2):
            problems = validate_row(row)
            if problems:
                rejected.append({"line": line_no, "problems": problems, "row": row})
            else:
                good_rows.append(row)

    init_db(db_path)
    save_rows(good_rows, db_path)
    return {"accepted": len(good_rows), "rejected": rejected}
