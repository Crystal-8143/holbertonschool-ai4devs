"""Cross-language specification compatibility tests for the Python baseline."""

import json
from pathlib import Path
import subprocess
import sys
import unittest

# Allows running the suite from the project root without an installed package.
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


class SpecCases(unittest.TestCase):
    """T01–T09: the exact nine fixtures documented in cross_language_spec.md."""

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_t01_empty_input(self):
        self.assertEqual(self.analyzer.analyze(""), expected())

    def test_t02_one_successful_request(self):
        source = log("203.0.113.10", target="/home", size=512)
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=512, status={"200": 1},
                                  paths=[("/home", 1)]))

    def test_t03_mixed_responses_and_query_stripping(self):
        source = "\n".join([
            log("203.0.113.10", target="/home", size=512),
            log("203.0.113.11", target="/home?ref=ad", status=404, size=100),
            log("203.0.113.10", method="POST", target="/api/items", status=500, size=0),
            log("203.0.113.12", target="/api/items", status=302, size=40),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(4, 3, 2, 50.0, 652, status={
                             "200": 1, "302": 1, "404": 1, "500": 1},
                                  paths=[("/api/items", 2), ("/home", 2)]))

    def test_t04_malformed_entry_is_ignored(self):
        source = log("198.51.100.7", target="/ok", size=10) + "\nnot an HTTP log record"
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=10, malformed=1,
                                  status={"200": 1}, paths=[("/ok", 1)]))

    def test_t05_missing_bytes_and_repeat_visitor(self):
        source = "\n".join([
            log("2001:db8::7", target="/health", status=204, size="-"),
            log("2001:db8::7", target="/oops", status=503, size=25),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(2, 1, 1, 50.0, 25,
                                  status={"204": 1, "503": 1},
                                  paths=[("/health", 1), ("/oops", 1)]))

    def test_t06_rounding_and_redirect(self):
        source = "\n".join([
            log("192.0.2.1", target="/x", status=301, size=3),
            log("192.0.2.2", target="/x?search=a", status=499, size=4),
            log("192.0.2.3", target="/y", status=599, size=4),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(3, 3, 2, 66.67, 11,
                                  status={"301": 1, "499": 1, "599": 1},
                                  paths=[("/x", 2), ("/y", 1)]))

    def test_t07_top_three_tie_breaking(self):
        source = "\n".join([log(target=f"/{path}") for path in "cabd"])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(4, 1, size=4, status={"200": 4},
                                  paths=[("/a", 1), ("/b", 1), ("/c", 1)]))

    def test_t08_invalid_status_bytes_and_method(self):
        source = "\n".join([
            log("192.0.2.8", target="/valid", size=9),
            log("192.0.2.8", target="/bad-status", status=700),
            log("192.0.2.8", target="/bad-bytes", size=-1),
            log("192.0.2.8", method="get", target="/bad-method"),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=9, malformed=3,
                                  status={"200": 1}, paths=[("/valid", 1)]))

    def test_t09_blank_line_and_trailing_lf(self):
        source = log("198.51.100.20", target="/ok") + "\n\n"
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=1, malformed=1,
                                  status={"200": 1}, paths=[("/ok", 1)]))


class ExtendedCases(unittest.TestCase):
    """Additional cases testing grammar, limits, newline handling, and CLI."""

    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_crlf_and_single_terminating_newline(self):
        source = log(target="/first") + "\r\n" + log(target="/second") + "\r\n"
        self.assertEqual(self.analyzer.analyze(source),
                         expected(2, 1, size=2, status={"200": 2},
                                  paths=[("/first", 1), ("/second", 1)]))

    def test_empty_line_is_malformed(self):
        self.assertEqual(self.analyzer.analyze("\n"), expected(malformed=1))
        self.assertEqual(self.analyzer.analyze("\n\n"), expected(malformed=2))

    def test_extra_spaces_and_combined_suffix_are_rejected(self):
        source = "\n".join([
            " " + log(), log() + " ", log().replace(" - - ", "  - - "),
            log() + ' "-" "Mozilla/5.0"', log(target="/valid"),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=1, malformed=4,
                                  status={"200": 1}, paths=[("/valid", 1)]))

    def test_status_boundaries(self):
        source = "\n".join([
            log(target="/a", status=100), log(target="/b", status=399),
            log(target="/c", status=400), log(target="/d", status=599),
            log(status=99), log(status=600),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(4, 1, 2, 50.0, 4, malformed=2,
                                  status={"100": 1, "399": 1, "400": 1, "599": 1},
                                  paths=[("/a", 1), ("/b", 1), ("/c", 1)]))

    def test_byte_value_limit_and_large_leading_zeroes(self):
        source = "\n".join([
            log(target="/max", size=MAX_SAFE_BYTES),
            log(target="/overflow", size=MAX_SAFE_BYTES + 1),
            log(target="/small", size="00004"),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(2, 1, size=MAX_SAFE_BYTES + 4, malformed=1,
                                  status={"200": 2},
                                  paths=[("/max", 1), ("/small", 1)]))
        self.assertIsNone(self.analyzer.parse_line(log(size="9" * 5000)))

    def test_round_half_up_at_exact_tie(self):
        # 1 error out of 32 requests = 3.125%; half-up means 3.13%, not 3.12%.
        source = "\n".join([log(status=400)] + [log() for _ in range(31)])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(32, 1, 1, 3.13, 32,
                                  status={"200": 31, "400": 1}, paths=[("/", 32)]))

    def test_case_sensitive_visitors_and_paths(self):
        source = "\n".join([
            log("CLIENT", target="/A"), log("client", target="/a"),
            log("CLIENT", target="/A?x=1"), log("CLIENT", target="/A/"),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(4, 2, size=4, status={"200": 4},
                                  paths=[("/A", 2), ("/A/", 1), ("/a", 1)]))

    def test_timestamp_shape_not_calendar_validity(self):
        valid_shape = log(timestamp="99/Zzz/0000:99:99:99 -9999")
        bad_shapes = [
            log(timestamp="9/Nov/2026:10:00:00 +1100"),
            log(timestamp="15/November/2026:10:00:00 +1100"),
            log(timestamp="15/Nov/2026:10:00:00 +11:00"),
        ]
        self.assertEqual(self.analyzer.analyze("\n".join([valid_shape] + bad_shapes)),
                         expected(1, 1, size=1, malformed=3,
                                  status={"200": 1}, paths=[("/", 1)]))

    def test_non_ascii_or_invalid_request_targets(self):
        source = "\n".join([
            log(target="/café"), log(target="not/a/path"),
            log(target='/bad"quote'), log(target="/bad path"),
            log(target="/ok?x=1?y=2"),
        ])
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=1, malformed=4,
                                  status={"200": 1}, paths=[("/ok", 1)]))

    def test_lone_cr_is_invalid_not_silently_trimmed(self):
        source = log(target="/good") + "\n" + log(target="/bad") + "\r"
        self.assertEqual(self.analyzer.analyze(source),
                         expected(1, 1, size=1, malformed=1,
                                  status={"200": 1}, paths=[("/good", 1)]))

    def test_cli_outputs_only_json(self):
        script = Path(__file__).resolve().parents[1] / "log_analyzer.py"
        source = log(target="/cli", size=7) + "\n"
        run = subprocess.run(
            [sys.executable, str(script)], input=source,
            text=True, capture_output=True, check=True,
        )
        self.assertEqual(run.stderr, "")
        self.assertEqual(json.loads(run.stdout),
                         expected(1, 1, size=7, status={"200": 1},
                                  paths=[("/cli", 1)]))


if __name__ == "__main__":
    unittest.main()
