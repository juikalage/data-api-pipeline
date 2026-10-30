"""Save and summarise transactions in SQLite."""

import sqlite3


def init_db(path: str) -> None:
    """Create the transactions table if it doesn't exist."""
    conn = sqlite3.connect(path)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )"""
    )
    conn.commit()
    conn.close()


def save_rows(rows: list[dict], path: str) -> None:
    """Insert or update valid rows."""
    init_db(path)
    conn = sqlite3.connect(path)
    conn.executemany(
        "INSERT OR REPLACE INTO transactions (transaction_id, amount, status) VALUES (?, ?, ?)",
        [(r["transaction_id"], float(r["amount"]), r["status"]) for r in rows],
    )
    conn.commit()
    conn.close()


def summary(path: str) -> dict:
    """Return count and total amount for each status."""
    init_db(path)
    conn = sqlite3.connect(path)
    cursor = conn.execute(
        "SELECT status, COUNT(*), SUM(amount) FROM transactions GROUP BY status ORDER BY status"
    )
    result = {status: {"count": count, "total": total} for status, count, total in cursor.fetchall()}
    conn.close()
    return result
