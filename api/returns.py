from fastapi import APIRouter
from models.full_returns_models import FullReturnsRequest
from core.full_returns_engine import calculate_nps_full, calculate_index_full

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Returns"]
)


@router.post("/returns:nps")
def nps_returns(request: FullReturnsRequest):
    return calculate_nps_full(request)


@router.post("/returns:index")
def index_returns(request: FullReturnsRequest):
    return calculate_index_full(request)