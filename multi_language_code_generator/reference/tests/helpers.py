"""Shared fixtures for the 20 independent HTTP log analyzer tests."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from log_analyzer import LogAnalyzer, MAX_SAFE_BYTES  # noqa: E402

TIMESTAMP = "15/Nov/2026:10:00:00 +1100"

def log(client="192.0.2.1", method="GET", target="/", status=200, size=1,
        timestamp=TIMESTAMP, version="1.1"):
    return (f'{client} - - [{timestamp}] "{method} {target} HTTP/{version}" '
            f'{status} {size}')


def expected(valid=0, visitors=0, errors=0, percent=0.0, size=0,
             malformed=0, status=None, paths=None):
    """Build the complete exact expected result, including empty fields."""
    return {
        "total_requests": valid,
        "unique_visitors": visitors,
        "error_requests": errors,
        "error_rate_percent": percent,
        "total_response_bytes": size,
        "malformed_lines": malformed,
        "status_counts": status if status is not None else {},
        "top_paths": ([{"path": path, "requests": count} for path, count in paths]
                      if paths is not None else []),
    }


class AnalyzerTestCase(unittest.TestCase):
    """Common setup used by each standalone test module."""

    def setUp(self):
        self.analyzer = LogAnalyzer()
