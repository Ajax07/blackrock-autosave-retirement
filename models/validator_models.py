from pydantic import BaseModel, Field
from typing import List
from models.transaction_model import Transaction


class TransactionValidatorRequest(BaseModel):
    wage: float = Field(gt=0)
    transactions: List[Transaction]
