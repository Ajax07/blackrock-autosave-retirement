# Test Type: Unit
# Validation: Verify k period aggregation
# Execution: pytest test/test_temporal_rules.py

from datetime import datetime
from core.aggregation_engine import aggregate_by_k


def test_k_aggregation():
    transactions = [
        {"timestamp": datetime(2023, 1, 1), "remanent": 50},
        {"timestamp": datetime(2023, 6, 1), "remanent": 100},
    ]

    class K:
        def __init__(self, start, end):
            self.start = start
            self.end = end

    k_periods = [
        K(datetime(2023, 1, 1), datetime(2023, 12, 31))
    ]

    result = aggregate_by_k(transactions, k_periods)

    assert result[0]["amount"] == 150
