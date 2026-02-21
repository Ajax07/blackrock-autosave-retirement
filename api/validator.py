from fastapi import APIRouter
from models.validator_models import TransactionValidatorRequest

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Transaction Validator"]
)


@router.post("/transactions:validator")
def validate_transactions(request: TransactionValidatorRequest):
    """
    Validates transactions based on:
    - duplicate timestamps
    - negative amounts
    - investment constraints based on wage
    """

    wage = request.wage
    transactions = request.transactions

    valid = []
    invalid = []
    seen_timestamps = set()

    # yearly investment limit (example business rule)
    annual_income = wage * 12
    max_investment_limit = min(0.10 * annual_income, 200000)

    total_investment = 0

    for tx in transactions:

        tx_dict = tx.model_dump()

        # duplicate check
        if tx.timestamp in seen_timestamps:
            invalid.append({
                **tx_dict,
                "message": "Duplicate timestamp"
            })
            continue

        seen_timestamps.add(tx.timestamp)

        # amount validation
        if tx.amount <= 0:
            invalid.append({
                **tx_dict,
                "message": "Amount must be positive"
            })
            continue

        # remanent validation
        if tx.remanent < 0:
            invalid.append({
                **tx_dict,
                "message": "Invalid remanent value"
            })
            continue

        # investment limit validation
        if total_investment + tx.remanent > max_investment_limit:
            invalid.append({
                **tx_dict,
                "message": "Exceeds investment limit based on wage"
            })
            continue

        total_investment += tx.remanent
        valid.append(tx)

    return {
        "valid": valid,
        "invalid": invalid,
        "maxInvestmentAllowed": max_investment_limit,
        "totalValidInvestment": total_investment
    }
