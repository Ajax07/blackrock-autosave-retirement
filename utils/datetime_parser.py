from datetime import datetime


def parse_datetime(ts: str):
    return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
