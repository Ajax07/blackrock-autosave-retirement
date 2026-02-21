from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class Expense(BaseModel):
    date: datetime
    amount: float = Field(gt=0)

    @field_validator("date", mode="before")
    def parse_date(cls, value):
        if isinstance(value, datetime):
            return value

        formats = [
            "%Y-%m-%d %H:%M:%S",   # space format
            "%Y-%m-%dT%H:%M:%S"    # ISO format
        ]

        for fmt in formats:
            try:
                return datetime.strptime(value, fmt)
            except:
                pass

        raise ValueError("Invalid datetime format")


class Transaction(BaseModel):
    timestamp: datetime
    amount: float
    ceiling: float
    remanent: float
