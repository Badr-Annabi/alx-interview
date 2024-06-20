#!/usr/bin/env python3
import sys
import re
import signal
from collections import defaultdict
from typing import Tuple, Optional

""" This Python script reads stdin line by line and computes metrics"""
"""<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>"""


def line_parser(line: str) -> Tuple[Optional[int], Optional[int]]:
    """This function Parses each line"""
    ip = r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)'
    date = r'(\d{2}/\d{2}/\d{4})'
    req = r'"GET /projects/260 HTTP/1\.1"'
    stat = r'(\d+)'
    file = r'(\d+)'
    pattern = rf'^ {ip} - \[{date}\] {req} {stat} {file}"$'
    compiled_pattern = re.compile(pattern)
    match = compiled_pattern.match(line)
    if match:
        file_size = int(match.group(4))
        status_code = int(match.group(3))
        return file_size, status_code
    else:
        return None, None


def print_stats(total_size: int, status_count: defaultdict) -> None:
    """This function prints the current stats"""
    print(f"File size: {total_size}")
    for code in sorted(status_count):
        print(f"{code}: {status_count[code]}")


def main() -> None:
    total_size: int = 0
    status_counts: defaultdict = defaultdict(int)
    line_count: int = 0

    try:
        for line in sys.stdin:
            line_count += 1
            file_size, status_code = line_parser(line.strip())

            if file_size is None or status_code is None:
                continue

            total_size += file_size
            status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
