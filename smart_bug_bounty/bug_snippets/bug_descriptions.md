# Bug Descriptions

## Overview

This folder contains six **intentionally flawed**, standalone examples for the Smart Bug Bounty exercise. Each snippet is 10–40 lines long and can be executed without third-party dependencies. The examples are intended for bug identification, explanation, and later repair; **do not treat the observed output as correct**.

| File | Language | Bug category | Intended behavior |
| --- | --- | --- | --- |
| `bug1.py` | Python | Off-by-one indexing | Return the last N activity entries in their original order. |
| `bug2.js` | JavaScript | Wrong calculation basis | Apply a percentage discount, then calculate tax on the discounted subtotal. |
| `bug3.java` | Java | Integer division | Return an accurate floating-point average of ratings. |
| `bug4.py` | Python | Shared mutable state | Build an independent report for every call. |
| `bug5.js` | JavaScript | Incorrect aggregation | Add each order's quantity to its product's units-sold total. |
| `bug6.java` | Java | Incorrect initial value | Return the maximum temperature, including when all readings are negative. |

## bug1.py — Recent activity list

- **Intended behavior:** `last_activities(activities, count)` returns exactly the last `count` entries, in original order. If `count` exceeds the list length, return all entries; if zero, return `[]`.
- **Current issue:** The slice starts one index too far to the right, so one expected item is omitted when `count` is within the list length.
- **Reproduction:** `last_activities(["login", "search", "view", "logout"], 2)`
- **Expected:** `["view", "logout"]`
- **Actual:** `["logout"]`
- **Run:** `python3 bug1.py`

## bug2.js — Invoice calculation

- **Intended behavior:** `invoiceTotal(subtotal, discountPercent, taxPercent)` deducts the discount, then applies tax to the discounted amount; return a currency total rounded to two decimals.
- **Current issue:** Tax is computed on the *original* subtotal instead of the discounted subtotal, so discounted invoices are overcharged whenever tax is positive.
- **Reproduction:** `invoiceTotal(100, 20, 10)`
- **Expected:** `88` (100 minus 20 discount, plus 8 tax)
- **Actual:** `90`
- **Run:** `node bug2.js`

## bug3.java — Average rating

- **Intended behavior:** `averageRating(ratings)` calculates the arithmetic mean, including any fractional part, as a `double`.
- **Current issue:** Both operands of the division are integers, so Java truncates the fractional part before returning the value as a `double`.
- **Reproduction:** `averageRating(new int[]{4, 5})`
- **Expected:** `4.5`
- **Actual:** `4.0`
- **Run:** `javac bug3.java && java bug3`

## bug4.py — Independent event reports

- **Intended behavior:** `build_report(events)` returns a new list of stripped event labels for each call; earlier and later reports must not affect each other.
- **Current issue:** The default report list is created only once and reused across calls, so data from the first call leaks into the second report (and mutates the first).
- **Reproduction:** Call `build_report(["started", "completed"])`, then `build_report(["failed"])`.
- **Expected second result:** `["failed"]`; the first result remains `["started", "completed"]`.
- **Actual second result:** `["started", "completed", "failed"]`; the first result is also changed.
- **Run:** `python3 bug4.py`

## bug5.js — Product units sold

- **Intended behavior:** `unitsSold(orders)` returns a mapping of product ID to the sum of ordered quantities, not the number of order records.
- **Current issue:** Each order record adds one unit regardless of its `quantity`, giving incorrect totals for multi-unit orders.
- **Reproduction:** Orders are `plant-a` quantity 3, `plant-b` quantity 1, `plant-a` quantity 2.
- **Expected:** `{ "plant-a": 5, "plant-b": 1 }`
- **Actual:** `{ "plant-a": 2, "plant-b": 1 }`
- **Run:** `node bug5.js`

## bug6.java — Highest temperature

- **Intended behavior:** `highestTemperature(readings)` returns the greatest integer reading, including values below zero.
- **Current issue:** The initial maximum is fixed at zero rather than a value from the input, so all-negative readings incorrectly return zero.
- **Reproduction:** `highestTemperature(new int[]{-7, -2, -5})`
- **Expected:** `-2`
- **Actual:** `0`
- **Run:** `javac bug6.java && java bug6`

## Suggested exercise workflow

1. Run each snippet and compare its actual output with the expected output above.
2. Identify the incorrect line and explain the failure mode.
3. Write a regression test that fails on the original code.
4. Fix the bug in a separate copy and confirm the regression test passes.

These snippets deliberately contain defects. Do not correct them in the submitted `bug_snippets/` folder unless a later assignment explicitly asks for fixed versions.
