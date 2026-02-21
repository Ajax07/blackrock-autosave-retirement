import time
import psutil
import threading


class PerformanceTracker:
    """
    Tracks system performance metrics.
    """

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def execution_time_ms(self):
        if self.start_time and self.end_time:
            return round((self.end_time - self.start_time) * 1000, 2)
        return 0

    def memory_usage_mb(self):
        process = psutil.Process()
        return round(process.memory_info().rss / 1024 / 1024, 2)

    def thread_count(self):
        return threading.active_count()
