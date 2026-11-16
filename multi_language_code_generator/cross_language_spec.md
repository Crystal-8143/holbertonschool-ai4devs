# Cross-Language Specification — HTTP Access Log Analyzer

## 1. Algorithm description

Build a deterministic log analyzer that parses **Apache Common Log Format–style** HTTP access records and reports traffic and error statistics. The same UTF-8 input must produce equivalent JSON data in every implementation language (for example, Python, JavaScript, and Java). No network access, external services, or third-party parsing libraries are required.

**Processing sequence:**

1. Read the entire input as UTF-8 text; process one physical line at a time.
2. Validate each record against the exact grammar and field rules below. Count invalid or blank records as malformed; continue processing remaining lines.
3. For valid records, count requests, distinct client tokens, HTTP error responses, response bytes, status codes, and normalized request paths.
4. Calculate the error rate and sort the top three paths using the specified ordering.
5. Return one JSON object with all required fields, even for empty input.

## 2. Input format

The input is a UTF-8 text string or file. Every nonempty line must have this format (one ASCII space between fields):

```text
CLIENT - - [DD/Mon/YYYY:HH:MM:SS ±HHMM] "METHOD /PATH HTTP/VERSION" STATUS BYTES
```

Example:

```text
203.0.113.10 - - [15/Nov/2026:10:00:00 +1100] "GET /home?ref=email HTTP/1.1" 200 512
```

**Field validation and normalization:**

| Field | Rule |
|---|---|
| `CLIENT` | Nonempty token of printable ASCII characters (U+0021–U+007E), with no whitespace, compared as an exact, case-sensitive string. It may be IPv4 or IPv6; do not resolve or validate IP addresses. |
| `- -` | Two literal hyphen placeholders, separated by single spaces. |
| Timestamp | Bracketed text in `DD/Mon/YYYY:HH:MM:SS ±HHMM` form: two-digit day, three ASCII letters for month, four-digit year, two-digit hour/minute/second, signed four-digit zone. Match the shape only; calendar validity is out of scope. |
| `METHOD` | One or more uppercase ASCII letters (`A`–`Z`). |
| Request target | Must start with `/` and contain only printable ASCII characters (U+0021–U+007E) other than double quotes, with no whitespace. For path aggregation, remove the first `?` and everything following it; do not percent-decode, lowercase, or remove trailing slashes. |
| `HTTP/VERSION` | Literal `HTTP/` followed by decimal digits, `.`, and decimal digits (such as `HTTP/1.1`). |
| `STATUS` | Exactly three decimal digits in the range `100`–`599`. |
| `BYTES` | Either `-` (meaning 0 bytes) or a nonnegative decimal integer in `0`–`9007199254740991`. |

Use LF (`\n`) or CRLF (`\r\n`) line endings. An empty input has zero lines; a terminating newline is **not** an extra blank line, but an actual empty line between two newline delimiters is malformed. Leading or trailing spaces in a record make it invalid. Records are otherwise treated literally; access logs with appended referrer/user-agent columns (Apache **Combined** format) are not accepted by this version.

## 3. Output format

Return a JSON object with this exact schema. All counts and byte totals are nonnegative integers; `error_rate_percent` is a JSON number.

```json
{
  "total_requests": 4,
  "unique_visitors": 3,
  "error_requests": 2,
  "error_rate_percent": 50.0,
  "total_response_bytes": 652,
  "malformed_lines": 0,
  "status_counts": { "200": 1, "302": 1, "404": 1, "500": 1 },
  "top_paths": [
    { "path": "/api/items", "requests": 2 },
    { "path": "/home", "requests": 2 }
  ]
}
```

| Field | Meaning |
|---|---|
| `total_requests` | Number of **valid** records. |
| `unique_visitors` | Count of distinct `CLIENT` tokens among valid records. |
| `error_requests` | Number of valid records with status `400`–`599` inclusive. |
| `error_rate_percent` | `100 × error_requests ÷ total_requests`, rounded to **two decimal places using round-half-up**; return `0.0` if no valid records. |
| `total_response_bytes` | Sum of valid `BYTES` values, treating `-` as 0. |
| `malformed_lines` | Number of invalid or blank input lines. |
| `status_counts` | Object whose keys are decimal status-code strings and values are their counts among valid records. An empty input yields `{}`. |
| `top_paths` | Up to three objects with normalized `path` and `requests`, ordered by descending request count, then ascending **case-sensitive ASCII lexicographic** path. |

For test comparison, parse JSON before comparing: object property order and optional trailing decimal zeros are not significant. Array ordering is significant. The algorithm must not print logs or extra text to standard output when JSON is expected.

## 4. Edge cases

- **Empty input:** all numeric fields are zero, `status_counts` is `{}`, and `top_paths` is `[]`.
- **Malformed input:** blank lines, incorrect field count, unsupported Combined-format suffix, invalid methods/status/byte values, or extra spaces are counted as malformed and excluded from all traffic statistics.
- **Repeated visitor:** the same exact `CLIENT` token counts as one unique visitor, even across multiple requests; two differently written tokens remain distinct.
- **Client address variety:** IPv4 and IPv6 are both accepted as opaque tokens.
- **Missing response size:** `BYTES` equal to `-` adds zero bytes without making the record invalid.
- **HTTP status classification:** `1xx`–`3xx` statuses are not errors; `4xx` and `5xx` are errors.
- **Paths with queries:** `/search?q=one` and `/search?q=two` both count under `/search`.
- **Ties and fewer than three paths:** paths sort alphabetically at equal frequencies; output may contain zero, one, or two paths.
- **Rounding:** percentages such as two out of three requests yield `66.67`, using base-10 round-half-up.
- **Very large byte values:** reject any single record's `BYTES` value above the specified limit. For test inputs, aggregate counts and totals fit within the same safe integer limit.

## 5. Test cases

Each block under **Input** represents the exact content of one UTF-8 input file, except T01, whose input is empty. **Expected output** is the complete JSON value to compare after parsing; formatting and object key order do not matter.

### T01 — Empty input

**Input:** empty file (0 bytes)

**Expected output:**

```json
{
  "total_requests": 0,
  "unique_visitors": 0,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 0,
  "malformed_lines": 0,
  "status_counts": {},
  "top_paths": []
}
```

**Checks:** No records or malformed lines.

### T02 — One successful request

**Input:**

```text
203.0.113.10 - - [15/Nov/2026:10:00:00 +1100] "GET /home HTTP/1.1" 200 512
```

**Expected output:**

```json
{
  "total_requests": 1,
  "unique_visitors": 1,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 512,
  "malformed_lines": 0,
  "status_counts": {
    "200": 1
  },
  "top_paths": [
    {
      "path": "/home",
      "requests": 1
    }
  ]
}
```

**Checks:** One visitor and one successful request.

### T03 — Mixed responses and query stripping

**Input:**

```text
203.0.113.10 - - [15/Nov/2026:10:00:00 +1100] "GET /home HTTP/1.1" 200 512
203.0.113.11 - - [15/Nov/2026:10:00:00 +1100] "GET /home?ref=ad HTTP/1.1" 404 100
203.0.113.10 - - [15/Nov/2026:10:00:00 +1100] "POST /api/items HTTP/1.1" 500 0
203.0.113.12 - - [15/Nov/2026:10:00:00 +1100] "GET /api/items HTTP/1.1" 302 40
```

**Expected output:**

```json
{
  "total_requests": 4,
  "unique_visitors": 3,
  "error_requests": 2,
  "error_rate_percent": 50.0,
  "total_response_bytes": 652,
  "malformed_lines": 0,
  "status_counts": {
    "200": 1,
    "302": 1,
    "404": 1,
    "500": 1
  },
  "top_paths": [
    {
      "path": "/api/items",
      "requests": 2
    },
    {
      "path": "/home",
      "requests": 2
    }
  ]
}
```

**Checks:** 404 and 500 are errors; 302 is not. Query strings do not create new paths.

### T04 — Malformed entry is ignored

**Input:**

```text
198.51.100.7 - - [15/Nov/2026:10:00:00 +1100] "GET /ok HTTP/1.1" 200 10
not an HTTP log record
```

**Expected output:**

```json
{
  "total_requests": 1,
  "unique_visitors": 1,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 10,
  "malformed_lines": 1,
  "status_counts": {
    "200": 1
  },
  "top_paths": [
    {
      "path": "/ok",
      "requests": 1
    }
  ]
}
```

**Checks:** Invalid record increments malformed_lines but does not stop processing.

### T05 — Missing byte value and repeat visitor

**Input:**

```text
2001:db8::7 - - [15/Nov/2026:10:00:00 +1100] "GET /health HTTP/1.1" 204 -
2001:db8::7 - - [15/Nov/2026:10:00:00 +1100] "GET /oops HTTP/1.1" 503 25
```

**Expected output:**

```json
{
  "total_requests": 2,
  "unique_visitors": 1,
  "error_requests": 1,
  "error_rate_percent": 50.0,
  "total_response_bytes": 25,
  "malformed_lines": 0,
  "status_counts": {
    "204": 1,
    "503": 1
  },
  "top_paths": [
    {
      "path": "/health",
      "requests": 1
    },
    {
      "path": "/oops",
      "requests": 1
    }
  ]
}
```

**Checks:** A dash means zero bytes; repeated IPv6 token counts as one visitor.

### T06 — Percentage rounding and redirect

**Input:**

```text
192.0.2.1 - - [15/Nov/2026:10:00:00 +1100] "GET /x HTTP/1.1" 301 3
192.0.2.2 - - [15/Nov/2026:10:00:00 +1100] "GET /x?search=a HTTP/1.1" 499 4
192.0.2.3 - - [15/Nov/2026:10:00:00 +1100] "GET /y HTTP/1.1" 599 4
```

**Expected output:**

```json
{
  "total_requests": 3,
  "unique_visitors": 3,
  "error_requests": 2,
  "error_rate_percent": 66.67,
  "total_response_bytes": 11,
  "malformed_lines": 0,
  "status_counts": {
    "301": 1,
    "499": 1,
    "599": 1
  },
  "top_paths": [
    {
      "path": "/x",
      "requests": 2
    },
    {
      "path": "/y",
      "requests": 1
    }
  ]
}
```

**Checks:** Two errors out of three requests yields 66.67%; 301 is not an error.

### T07 — Top-three tie-breaking

**Input:**

```text
192.0.2.1 - - [15/Nov/2026:10:00:00 +1100] "GET /c HTTP/1.1" 200 1
192.0.2.1 - - [15/Nov/2026:10:00:00 +1100] "GET /a HTTP/1.1" 200 1
192.0.2.1 - - [15/Nov/2026:10:00:00 +1100] "GET /b HTTP/1.1" 200 1
192.0.2.1 - - [15/Nov/2026:10:00:00 +1100] "GET /d HTTP/1.1" 200 1
```

**Expected output:**

```json
{
  "total_requests": 4,
  "unique_visitors": 1,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 4,
  "malformed_lines": 0,
  "status_counts": {
    "200": 4
  },
  "top_paths": [
    {
      "path": "/a",
      "requests": 1
    },
    {
      "path": "/b",
      "requests": 1
    },
    {
      "path": "/c",
      "requests": 1
    }
  ]
}
```

**Checks:** Four paths tied at one request: return /a, /b, /c only.

### T08 — Invalid status, negative byte count, and lowercase method

**Input:**

```text
192.0.2.8 - - [15/Nov/2026:10:00:00 +1100] "GET /valid HTTP/1.1" 200 9
192.0.2.8 - - [15/Nov/2026:10:00:00 +1100] "GET /bad-status HTTP/1.1" 700 1
192.0.2.8 - - [15/Nov/2026:10:00:00 +1100] "GET /bad-bytes HTTP/1.1" 200 -1
192.0.2.8 - - [15/Nov/2026:10:00:00 +1100] "get /bad-method HTTP/1.1" 200 1
```

**Expected output:**

```json
{
  "total_requests": 1,
  "unique_visitors": 1,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 9,
  "malformed_lines": 3,
  "status_counts": {
    "200": 1
  },
  "top_paths": [
    {
      "path": "/valid",
      "requests": 1
    }
  ]
}
```

**Checks:** Three malformed entries do not alter the statistics for the valid entry.

### T09 — Blank line and trailing newline

**Input:** exactly the single log record below followed by **two LF newline characters** (`\n\n`), yielding one blank line after the record.

```text
198.51.100.20 - - [15/Nov/2026:10:00:00 +1100] "GET /ok HTTP/1.1" 200 1
```

**Expected output:**

```json
{
  "total_requests": 1,
  "unique_visitors": 1,
  "error_requests": 0,
  "error_rate_percent": 0.0,
  "total_response_bytes": 1,
  "malformed_lines": 1,
  "status_counts": {
    "200": 1
  },
  "top_paths": [
    {
      "path": "/ok",
      "requests": 1
    }
  ]
}
```

**Checks:** The interior blank record is malformed; the final newline does not create a phantom extra record.