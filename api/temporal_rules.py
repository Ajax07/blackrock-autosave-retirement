from fastapi import APIRouter
from typing import List
from models.transaction_model import Transaction
from models.period_models import QPeriod, PPeriod, KPeriod
from core.period_engine import apply_period_rules
from core.aggregation_engine import aggregate_by_k

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Temporal Rules"]
)


@router.post("/transactions:filter")
def apply_temporal_rules(
    transactions: List[Transaction],
    q: List[QPeriod] = [],
    p: List[PPeriod] = [],
    k: List[KPeriod] = []
):
    tx_dicts = [t.model_dump() for t in transactions]

    # apply q and p rules
    processed = apply_period_rules(tx_dicts, q, p)

    # group by k periods
    grouped = aggregate_by_k(processed, k)

    return {
        "processed_transactions": processed,
        "savings_by_period": grouped
    }
