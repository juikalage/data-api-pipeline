from src.storage import save_rows, summary


def test_save_and_summarise(tmp_path):
    db = str(tmp_path / "test.db")
    rows = [
        {"transaction_id": "T1", "amount": "10", "status": "paid"},
        {"transaction_id": "T2", "amount": "5.5", "status": "paid"},
        {"transaction_id": "T3", "amount": "7", "status": "failed"},
    ]
    save_rows(rows, db)

    result = summary(db)

    assert result["paid"]["count"] == 2
    assert result["paid"]["total"] == 15.5
    assert result["failed"]["count"] == 1
