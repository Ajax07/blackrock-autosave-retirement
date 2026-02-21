from fastapi import APIRouter
from typing import List
from models.transaction_model import Transaction

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Transaction Validator"]
)


@router.post("/transactions:validator")
def validate_transactions(transactions: List[Transaction]):
    valid = []
    invalid = []

    seen_timestamps = set()

    for tx in transactions:

        # duplicate timestamp check
        if tx.timestamp in seen_timestamps:
            invalid.append({
                **tx.model_dump(),
                "message": "Duplicate timestamp"
            })
            continue

        seen_timestamps.add(tx.timestamp)

        # amount validation
        if tx.amount <= 0:
            invalid.append({
                **tx.model_dump(),
                "message": "Amount must be positive"
            })
            continue

        valid.append(tx)

    return {
        "valid": valid,
        "invalid": invalid
    }
