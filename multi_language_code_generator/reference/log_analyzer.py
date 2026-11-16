"""Deterministic Apache Common Log Format-style access log analyzer.

This is the Python reference implementation of ../cross_language_spec.md.
It uses only the Python standard library and requires Python 3.10+.

Usage:
    python reference/log_analyzer.py access.log
    cat access.log | python reference/log_analyzer.py
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from typing import Any, Iterator

MAX_SAFE_BYTES = 9_007_199_254_740_991
_MAX_SAFE_BYTES_TEXT = str(MAX_SAFE_BYTES)

# A client is an arbitrary printable ASCII token (not necessarily an IP address).
# The target permits printable ASCII except double quotes, with no whitespace.
# Date/time shape is checked, but calendar validity intentionally is not.
LOG_PATTERN = re.compile(
    r'(?P<client>[!-~]+) - - '
    r'\[[0-9]{2}/[A-Za-z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2} [+-][0-9]{4}\] '
    r'"(?P<method>[A-Z]+) (?P<target>/[!#-~]*) HTTP/[0-9]+\.[0-9]+" '
    r'(?P<status>[0-9]{3}) (?P<bytes>-|[0-9]+)',
    flags=re.ASCII,
)


class LogAnalyzer:
    """Parse strict access-log records and calculate specified summary statistics."""

    def parse_line(self, line: str) -> dict[str, str | int] | None:
        """Return normalized values for a valid *record*, or None if malformed.

        The supplied line must not contain a line terminator. Method, client,
        target, and timestamp are validated according to the specification.
        """
        match = LOG_PATTERN.fullmatch(line)
        if match is None:
            return None

        status = int(match.group("status"))
        if not 100 <= status <= 599:
            return None

        raw_bytes = match.group("bytes")
        if raw_bytes == "-":
            byte_count = 0
        else:
            # Compare strings first to avoid Python's large-integer digit limit
            # for arbitrarily long malformed input values.
            canonical = raw_bytes.lstrip("0") or "0"
            if (
                len(canonical) > len(_MAX_SAFE_BYTES_TEXT)
                or (
                    len(canonical) == len(_MAX_SAFE_BYTES_TEXT)
                    and canonical > _MAX_SAFE_BYTES_TEXT
                )
            ):
                return None
            byte_count = int(canonical)

        return {
            "client": match.group("client"),
            "method": match.group("method"),
            "path": match.group("target").split("?", 1)[0],
            "status": status,
            "bytes": byte_count,
        }

    @staticmethod
    def _records(text: str) -> Iterator[str]:
        """Split only at LF; remove CR *only* if part of a CRLF terminator.

        A final LF (or CRLF) does not add a phantom blank record, whereas an
        actual blank line is yielded and counted as malformed. Lone CRs are
        left in records and will fail validation.
        """
        if not text:
            return

        parts = text.split("\n")
        terminates_with_lf = text.endswith("\n")
        if terminates_with_lf:
            parts.pop()

        for index, part in enumerate(parts):
            has_terminator = index < len(parts) - 1 or terminates_with_lf
            if has_terminator and part.endswith("\r"):
                part = part[:-1]
            yield part

    def analyze(self, text: str) -> dict[str, Any]:
        """Analyze UTF-8-decoded text and return JSON-serializable statistics.

        Error-rate rounding uses integer arithmetic to implement exact
        decimal round-half-up at two places, not Python's round-to-even.
        """
        visitors: set[str] = set()
        status_counts: Counter[str] = Counter()
        path_counts: Counter[str] = Counter()
        valid = errors = total_bytes = malformed = 0

        for line in self._records(text):
            record = self.parse_line(line)
            if record is None:
                malformed += 1
                continue

            valid += 1
            visitors.add(str(record["client"]))
            status = int(record["status"])
            status_counts[str(status)] += 1
            path_counts[str(record["path"])] += 1
            total_bytes += int(record["bytes"])
            if status >= 400:
                errors += 1

        # Percentage: errors * 100, then 2 decimal places => * 10_000.
        # floor(x + 0.5) on the positive rational implements round-half-up.
        hundredths = (2 * errors * 10_000 + valid) // (2 * valid) if valid else 0
        error_rate = hundredths / 100

        top_paths = [
            {"path": path, "requests": count}
            for path, count in sorted(
                path_counts.items(), key=lambda item: (-item[1], item[0])
            )[:3]
        ]

        return {
            "total_requests": valid,
            "unique_visitors": len(visitors),
            "error_requests": errors,
            "error_rate_percent": error_rate,
            "total_response_bytes": total_bytes,
            "malformed_lines": malformed,
            "status_counts": dict(sorted(status_counts.items(), key=lambda item: int(item[0]))),
            "top_paths": top_paths,
        }


def main(argv: list[str] | None = None) -> int:
    """Read a UTF-8 file, or standard input, and print one JSON object."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "logfile", nargs="?", type=Path,
        help="UTF-8 access-log file (omit to read from standard input)",
    )
    args = parser.parse_args(argv)

    try:
        if args.logfile is not None:
            with args.logfile.open("r", encoding="utf-8", newline="") as source:
                text = source.read()
        else:
            text = sys.stdin.buffer.read().decode("utf-8")
    except (OSError, UnicodeError) as exc:
        parser.exit(status=2, message=f"Unable to read UTF-8 log: {exc}\n")

    print(json.dumps(LogAnalyzer().analyze(text), ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
