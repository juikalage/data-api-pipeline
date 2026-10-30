from src.validate import validate_row


def test_valid_row_has_no_problems():
    row = {"transaction_id": "T1", "amount": "250.00", "status": "paid"}
    assert validate_row(row) == []


def test_missing_column_is_reported():
    row = {"transaction_id": "T2", "amount": "100", "status": ""}
    assert "missing status" in validate_row(row)


def test_bad_amount_is_reported():
    row = {"transaction_id": "T3", "amount": "abc", "status": "paid"}
    assert "amount is not a number" in validate_row(row)


def test_unknown_status_is_reported():
    row = {"transaction_id": "T4", "amount": "10", "status": "refunded"}
    assert any("unknown status" in p for p in validate_row(row))
