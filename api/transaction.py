from fastapi import APIRouter
from typing import List

from models.transaction_model import Expense
from core.rounding_engine import round_to_100

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Transactions"]
)


@router.post("/transactions:parse")
def parse_transactions(expenses: List[Expense]):
    results = []

    for e in expenses:
        ceiling, rem = round_to_100(e.amount)

        results.append({
            "timestamp": e.date,
            "amount": e.amount,
            "ceiling": ceiling,
            "remanent": rem
        })

    return results
