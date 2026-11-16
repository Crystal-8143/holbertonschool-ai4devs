# Python Reference Implementation — HTTP Access Log Analyzer

This baseline implements the companion `../cross_language_spec.md` for the
`holbertonschool-ai4devs/multi_language_code_generator` assignment. It has no
external dependencies and requires **Python 3.10+**.

## Project layout

```text
multi_language_code_generator/
├── cross_language_spec.md              # From the previous assignment
└── reference/
    ├── log_analyzer.py
    ├── README.md
    └── tests/
        └── test_log_analyzer.py
```

## Run

From the `multi_language_code_generator/` directory:

```bash
python reference/log_analyzer.py path/to/access.log
```

Or pipe UTF-8 logs through standard input:

```bash
cat path/to/access.log | python reference/log_analyzer.py
```

The command prints exactly one JSON object to standard output. An unreadable
file or invalid UTF-8 causes a nonzero exit and diagnostic on standard error.

## Run all tests

From the `multi_language_code_generator/` directory:

```bash
python -m unittest discover -s reference/tests -p 'test_*.py' -v
```

The tests verify **all nine cases in the specification** plus additional
cases, including CRLF line endings, half-up rounding, numeric bounds, invalid
records, case sensitivity, strict grammar, and the command-line interface.

## Python API

```python
from reference.log_analyzer import LogAnalyzer

analyzer = LogAnalyzer()
result = analyzer.analyze(
    '203.0.113.10 - - [15/Nov/2026:10:00:00 +1100] '
    '"GET /home HTTP/1.1" 200 512\n'
)
assert result['total_requests'] == 1
```

`LogAnalyzer.parse_line(line)` returns a normalized dictionary for a valid
record, or `None` for a malformed record. `LogAnalyzer.analyze(text)` returns
the exact JSON-serializable schema defined by the specification.

## Cross-language consistency

- Only Apache Common-style records matching the strict specification count.
- Blank or invalid records are malformed and excluded from request statistics.
- Visitor identity and normalized paths are case-sensitive.
- Percentages use decimal **round-half-up**, not a language's default rounding.
- The three most frequent paths sort by descending count, then ASCII name.
- For all test inputs, aggregate byte totals remain below the safe-integer limit.
