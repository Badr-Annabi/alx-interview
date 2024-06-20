#!/usr/bin/env python3
import sys

""" This Python script reads stdin line by line and computes metrics"""
"""<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>"""

if __name__ == "__main__":
    file_size, line_count = 0, 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_count = {k: 0 for k in status_codes}

    def print_stats(total_size: int, status_count: dict) -> None:
        """This function prints the current stats"""
        print("File size: {:d}".format(total_size))
        for k, v in sorted(status_count.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                file_size += int(data[-1])
                status_code = data[-2]
                if status_code in status_count:
                    status_count[status_code] += 1
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(file_size, status_count)
        print_stats(file_size, status_count)
    except KeyboardInterrupt:
        print_stats(file_size, status_count)
        raise
