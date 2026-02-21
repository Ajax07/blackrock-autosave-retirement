from fastapi import APIRouter
from utils.performance_tracker import PerformanceTracker

router = APIRouter(
    prefix="/blackrock/challenge/v1",
    tags=["Performance"]
)

tracker = PerformanceTracker()


@router.get("/performance")
def performance_report():
    tracker.start()
    tracker.stop()

    return {
        "time_ms": tracker.execution_time_ms(),
        "memory_mb": tracker.memory_usage_mb(),
        "threads": tracker.thread_count()
    }
