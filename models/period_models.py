from pydantic import BaseModel
from datetime import datetime


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
