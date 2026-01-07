# src/parser.py
import re
from typing import List
from .models import LogEntry

LOG_PATTERN = re.compile(
    r"(?P<remote_addr>[\d\.]+) - - \[(?P<time_local>.*?)\] "
    r'"(?P<method>\w+) (?P<url>\S+) \S+" (?P<status>\d+) (?P<body_bytes_sent>\d+) '
    r'"(?P<http_referer>.*?)" "(?P<http_user_agent>.*?)" (?P<request_time>[\d\.]+)'
)


def parse_log_line(line: str) -> LogEntry | None:
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    return LogEntry(
        method=data["method"],
        url=data["url"],
        status=int(data["status"]),
        request_time=float(data["request_time"]),
    )


def parse_log_file(filepath: str) -> List[LogEntry]:
    entries = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            entry = parse_log_line(line.strip())
            if entry:
                entries.append(entry)
    return entries
