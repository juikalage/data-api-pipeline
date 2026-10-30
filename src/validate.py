"""Validate transaction rows before they are stored."""

REQUIRED_COLUMNS = ["transaction_id", "amount", "status"]
VALID_STATUSES = {"paid", "pending", "failed"}


def validate_row(row: dict) -> list[str]:
    """Return a list of problems with one row. An empty list means the row is valid."""
    problems = []

    for col in REQUIRED_COLUMNS:
        if not row.get(col):
            problems.append(f"missing {col}")

    try:
        float(row.get("amount", ""))
    except (TypeError, ValueError):
        problems.append("amount is not a number")

    if row.get("status") not in VALID_STATUSES:
        problems.append(f"unknown status: {row.get('status')}")

    return problems
