# Data API Pipeline

A Python pipeline that loads transaction data from a CSV file, validates each row, stores the valid rows in SQLite, and exposes a summary through a FastAPI endpoint.

## Features

- Validates each row: required columns, numeric amount, and known status values
- Separates accepted rows from rejected rows, with the reason for each rejection
- Stores accepted rows in SQLite, updating any row with a repeated transaction ID
- Serves a `/summary` endpoint with the count and total amount per status
- Automated tests with pytest, run on every push with GitHub Actions

## Project structure
