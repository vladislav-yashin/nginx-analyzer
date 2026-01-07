# src/analyzer.py
import statistics
from typing import List, Dict
from .models import LogEntry


def generate_report(entries: List[LogEntry]) -> Dict:
    if not entries:
        return {"error": "No valid log entries found"}

    times = [entry.request_time for entry in entries]

    return {
        "total_requests": len(entries),
        "average_request_time": round(statistics.mean(times), 4),
        "median_request_time": round(statistics.median(times), 4),
        "p95_request_time": round(sorted(times)[int(0.95 * len(times))], 4),
        "slowest_request_time": round(max(times), 4),
        "fastest_request_time": round(min(times), 4),
    }
