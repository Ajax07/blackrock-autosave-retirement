from fastapi import APIRouter
from models.filter_models import TemporalFilterRequest
from core.rounding_engine import round_to_100
from core.period_engine import apply_period_rules
from core.aggregation_engine import aggregate_by_k
from datetime import datetime

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Temporal Rules"]
)


@router.post("/transactions:filter")
def apply_temporal_rules(request: TemporalFilterRequest):

    # STEP 1 — convert raw expenses → transactions
    transactions = []

    for exp in request.transactions:
        ceiling, rem = round_to_100(exp.amount)

        transactions.append({
            "timestamp": exp.date,
            "amount": exp.amount,
            "ceiling": ceiling,
            "remanent": rem
        })

    # STEP 2 — apply q/p rules
    processed = apply_period_rules(transactions, request.q, request.p)

    # STEP 3 — group by k periods
    grouped = aggregate_by_k(processed, request.k)

    return {
        "processed_transactions": processed,
        "savings_by_period": grouped
    }
