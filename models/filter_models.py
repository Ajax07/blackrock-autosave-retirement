from pydantic import BaseModel
from typing import List
from datetime import datetime


class Expense(BaseModel):
    date: datetime
    amount: float


class QPeriod(BaseModel):
    fixed: float
    start: datetime
    end: datetime


class PPeriod(BaseModel):
    extra: float
    start: datetime
    end: datetime


class KPeriod(BaseModel):
    start: datetime
    end: datetime


class TemporalFilterRequest(BaseModel):
    wage: float
    transactions: List[Expense]
    q: List[QPeriod] = []
    p: List[PPeriod] = []
    k: List[KPeriod] = []
