from fastapi import APIRouter
from services.projection_service import investment_projection

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Returns"]
)


@router.post("/returns:index")
def calculate_index_return(amount: float, age: int, inflation: float):
    rate = 0.1449
    return investment_projection(amount, rate, age, inflation)


@router.post("/returns:nps")
def calculate_nps_return(amount: float, age: int, inflation: float):
    rate = 0.0711
    return investment_projection(amount, rate, age, inflation)
