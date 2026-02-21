from pydantic import BaseModel, Field
from datetime import datetime


class Expense(BaseModel):
    date: datetime
    amount: float = Field(gt=0)


class Transaction(BaseModel):
    timestamp: datetime
    amount: float
    ceiling: float
    remanent: float
