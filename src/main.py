# src/main.py
import argparse
import json
from .parser import parse_log_file
from .analyzer import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Analyze nginx log and generate report"
    )
    parser.add_argument("log_file", help="Path to nginx access log")
    parser.add_argument(
        "--output", default="reports/report.json", help="Output report path"
    )
    args = parser.parse_args()

    entries = parse_log_file(args.log_file)
    report = generate_report(entries)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"Report generated: {args.output}")


if __name__ == "__main__":
    main()
