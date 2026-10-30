from src.pipeline import run_pipeline
from src.storage import summary


def test_pipeline_accepts_valid_and_rejects_bad_rows(tmp_path):
    csv_file = tmp_path / "input.csv"
    csv_file.write_text(
        "transaction_id,amount,status\n"
        "T1,250.00,paid\n"
        "T2,abc,paid\n"
        "T3,10,refunded\n"
        "T4,30,failed\n",
        encoding="utf-8",
    )
    db = str(tmp_path / "test.db")

    result = run_pipeline(str(csv_file), db)

    assert result["accepted"] == 2
    assert len(result["rejected"]) == 2
    assert summary(db)["failed"]["count"] == 1
