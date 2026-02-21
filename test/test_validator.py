# Test Type: Unit
# Validation: Verify rounding to next multiple of 100
# Execution: pytest test/test_rounding.py

from core.rounding_engine import round_to_100


def test_rounding_basic():
    ceiling, rem = round_to_100(1519)
    assert ceiling == 1600
    assert rem == 81


def test_rounding_exact_multiple():
    ceiling, rem = round_to_100(500)
    assert ceiling == 500
    assert rem == 0


def test_rounding_small_value():
    ceiling, rem = round_to_100(1)
    assert ceiling == 100
    assert rem == 99
