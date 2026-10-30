from fastapi.testclient import TestClient

from src import config
from src.api import app
from src.pipeline import run_pipeline


def test_summary_endpoint(tmp_path, monkeypatch):
    db = str(tmp_path / "api.db")
    monkeypatch.setattr(config, "DB_PATH", db)

    csv_file = tmp_path / "input.csv"
    csv_file.write_text(
        "transaction_id,amount,status\nT1,100,paid\nT2,50,paid\n",
        encoding="utf-8",
    )
    run_pipeline(str(csv_file), db)

    client = TestClient(app)
    response = client.get("/summary")

    assert response.status_code == 200
    assert response.json()["paid"]["count"] == 2
    assert response.json()["paid"]["total"] == 150.0
