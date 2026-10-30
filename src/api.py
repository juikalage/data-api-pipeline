"""FastAPI service that exposes transaction summaries."""

from fastapi import FastAPI

from src import config
from src.storage import summary

app = FastAPI(title="Data API Pipeline")


@app.get("/summary")
def get_summary() -> dict:
    """Return count and total amount per status."""
    return summary(config.DB_PATH)
