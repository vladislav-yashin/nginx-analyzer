from dataclasses import dataclass

@dataclass
class LogEntry:
    method: str
    url: str
    status: int
    request_time: float
