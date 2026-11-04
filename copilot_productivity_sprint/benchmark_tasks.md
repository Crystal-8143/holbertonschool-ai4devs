# Benchmark Tasks

Four varied tasks, each solvable in 15–30 minutes. They cover a backend endpoint, algorithmic logic, data processing, and testing/refactoring so that Copilot's help can be compared across different kinds of work.

Suggested language: Python 3 (Flask/FastAPI for Task 1) or Node.js. Use the same language for the manual and Copilot-assisted attempts.

---

## Task 1 - CRUD Endpoint
**Time budget**: 25–30 min | **Category**: Backend / API

**Requirements**: Implement `POST /users` with input validation. Store users in memory (a list or dict is fine). Each user gets a unique auto-incrementing ID. Reject duplicate emails.

**Inputs**: JSON body `{ "name": string, "email": string }`

**Outputs**: JSON `{ "id": int, "name": string, "email": string }`

**Acceptance Criteria**:
- Returns `201` and the stored user with an ID on success
- Returns `400` if `name` is missing or empty
- Returns `400` if `email` is missing or not a valid email format
- Returns `409` if the email already exists
- IDs are unique and increase with each created user
- At least 4 automated tests cover the cases above

---

## Task 2 - Algorithm: Longest Substring Without Repeating Characters
**Time budget**: 15–20 min | **Category**: Algorithms

**Requirements**: Write a function `longest_unique_substring(s)` that returns the length of the longest substring containing no repeated characters. The solution must run in O(n) time using a sliding window.

**Inputs**: A string `s` (0 to 100,000 characters, any ASCII characters)

**Outputs**: An integer, the length of the longest substring without repeats

**Acceptance Criteria**:
- `"abcabcbb"` returns `3`
- `"bbbbb"` returns `1`
- `"pwwkew"` returns `3`
- `""` returns `0`
- Handles a 100,000-character input in under 1 second
- Includes a short docstring stating time and space complexity

---

## Task 3 - Data Processing: CSV Sales Summary
**Time budget**: 20–25 min | **Category**: Data / File I/O

**Requirements**: Write a script `summarize_sales.py` that reads a CSV of sales records and prints a summary report. Skip and count malformed rows instead of crashing.

**Inputs**: CSV file path as a command-line argument. Columns: `date` (YYYY-MM-DD), `product`, `quantity` (int), `unit_price` (float).

Example:
```csv
date,product,quantity,unit_price
2024-01-05,Widget,10,2.50
2024-01-06,Gadget,3,10.00
2024-01-06,Widget,5,2.50
```

**Outputs**: Printed report (or JSON) containing:
- Total revenue
- Revenue per product, sorted highest first
- Best-selling product by quantity
- Number of malformed rows skipped

**Acceptance Criteria**:
- For the example above, total revenue is `67.50`
- Revenue per product: Widget `37.50`, Gadget `30.00`
- Rows with missing fields, non-numeric quantity/price, or negative values are skipped and counted
- Missing file produces a clear error message and a non-zero exit code
- Empty file (header only) outputs total revenue `0.00` without errors

---

## Task 4 - Refactor and Test Legacy Code
**Time budget**: 20–25 min | **Category**: Refactoring / Testing

**Requirements**: Given the function below, refactor it for readability and correctness, then add unit tests. Behavior must stay the same except for the bug fixes listed.

```python
def calc(l, t):
    r = 0
    for i in range(len(l)):
        if t == 'a':
            r = r + l[i]
        elif t == 'm':
            if i == 0: r = 1
            r = r * l[i]
        elif t == 'x':
            if l[i] > r: r = l[i]
    return r
```

**Inputs**: A list of numbers and an operation code: `'a'` (sum), `'m'` (product), `'x'` (maximum)

**Outputs**: A number, the result of the operation

**Acceptance Criteria**:
- Function and parameter names are descriptive, with type hints and a docstring
- Unknown operation codes raise `ValueError`
- Maximum works for lists of all-negative numbers (the original returns `0`, which is a bug)
- Empty list behavior is defined and tested: sum is `0`, product is `1`, maximum raises `ValueError`
- At least 6 unit tests pass, covering each operation, negatives, empty list, and invalid code
- No loop uses `range(len(...))`

---

## Scoring Guide (for comparing manual vs. Copilot-assisted attempts)

| Metric | How to measure |
|--------|----------------|
| Time to completion | Stopwatch from start to all acceptance criteria met |
| Acceptance criteria passed | Count of criteria satisfied on the first run |
| Number of prompts / edits | Copilot prompts used, manual corrections made |
| Code quality | Readability, naming, structure (1–5) |
| Bugs found after "done" | Issues discovered during review |