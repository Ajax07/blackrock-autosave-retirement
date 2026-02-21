from fastapi import APIRouter
from models.filter_models import TemporalFilterRequest
from core.rounding_engine import round_to_100
from core.period_engine import apply_period_rules
from core.aggregation_engine import aggregate_by_k

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Temporal Rules"]
)


@router.post("/transactions:filter")
def apply_temporal_rules(request: TemporalFilterRequest):
    """
    Full temporal constraints validator:
    - rejects duplicate timestamps
    - rejects negative amounts
    - applies q/p rules
    - aggregates by k periods
    """

    valid_transactions = []
    invalid_transactions = []
    seen_timestamps = set()

    # STEP 1 — Validate + convert expenses → transactions
    for exp in request.transactions:

        # negative amount check
        if exp.amount <= 0:
            invalid_transactions.append({
                "date": exp.date,
                "amount": exp.amount,
                "message": "Negative or zero amount not allowed"
            })
            continue

        # duplicate timestamp check
        if exp.date in seen_timestamps:
            invalid_transactions.append({
                "date": exp.date,
                "amount": exp.amount,
                "message": "Duplicate timestamp not allowed"
            })
            continue

        seen_timestamps.add(exp.date)

        ceiling, rem = round_to_100(exp.amount)

        valid_transactions.append({
            "timestamp": exp.date,
            "amount": exp.amount,
            "ceiling": ceiling,
            "remanent": rem
        })

    # STEP 2 — apply q/p rules only to valid transactions
    processed = apply_period_rules(valid_transactions, request.q, request.p)

    # STEP 3 — group by k periods
    grouped = aggregate_by_k(processed, request.k)

    return {
        "valid_transactions": processed,
        "invalid_transactions": invalid_transactions,
        "savings_by_period": grouped
    }