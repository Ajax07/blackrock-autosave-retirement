# Load test for 1M transactions
# Execution: locust -f load_test/locustfile.py

from locust import HttpUser, task


class TransactionUser(HttpUser):

    @task
    def parse_transactions(self):
        payload = [
            {"date": "2023-10-12T20:15:00", "amount": 250}
        ] * 1000

        self.client.post(
            "/blackrock/challenge/v1/transactions:parse",
            json=payload
        )
