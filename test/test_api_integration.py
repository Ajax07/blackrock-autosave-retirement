# Test Type: Integration
# Validation: Test transaction parse endpoint
# Execution: pytest test/test_api_integration.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_parse_transactions_api():
    payload = [
        {"date": "2023-10-12T20:15:00", "amount": 250}
    ]

    response = client.post(
        "/blackrock/challenge/v1/transactions:parse",
        json=payload
    )

    assert response.status_code == 200
    assert response.json()[0]["ceiling"] == 300
