from core.rounding_engine import round_to_100
from core.period_engine import apply_period_rules
from core.aggregation_engine import aggregate_by_k
from services.projection_service import investment_projection

RETIREMENT_AGE = 60
NPS_RATE = 0.0711
INDEX_RATE = 0.1449


def process_full_pipeline(request, rate):
    valid_transactions = []
    invalid_transactions = []
    seen = set()

    # STEP 1 — validate + round
    for exp in request.transactions:

        if exp.amount <= 0:
            invalid_transactions.append({
                "date": exp.date,
                "amount": exp.amount,
                "message": "Negative amount not allowed"
            })
            continue

        if exp.date in seen:
            invalid_transactions.append({
                "date": exp.date,
                "amount": exp.amount,
                "message": "Duplicate timestamp not allowed"
            })
            continue

        seen.add(exp.date)

        ceiling, rem = round_to_100(exp.amount)

        valid_transactions.append({
            "timestamp": exp.date,
            "amount": exp.amount,
            "ceiling": ceiling,
            "remanent": rem
        })

    # STEP 2 — apply temporal rules
    processed = apply_period_rules(valid_transactions, request.q, request.p)

    # STEP 3 — aggregate by k periods
    grouped = aggregate_by_k(processed, request.k)

    total_investment = sum(tx["remanent"] for tx in processed)

    # STEP 4 — calculate returns
    years = RETIREMENT_AGE - request.age

    result = investment_projection(
        total_investment,
        rate,
        years,
        request.inflation / 100
    )

    return {
        "valid_transactions": processed,
        "invalid_transactions": invalid_transactions,
        "total_investment": total_investment,
        "investment_breakdown": grouped,
        "returns": result
    }


def calculate_nps_full(request):
    return process_full_pipeline(request, NPS_RATE)


def calculate_index_full(request):
    return process_full_pipeline(request, INDEX_RATE)