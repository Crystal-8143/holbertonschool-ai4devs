# Fix Validation Report

**Project:** Holberton School AI4Devs — Smart Bug Bounty  
**Directory:** `smart_bug_bounty/bug_fixes/`  
**Validation date:** 2026-11-17  
**Languages:** Python, JavaScript, Java  
**Result:** **37 / 37 automated tests passed; 0 failures.**

## Method

The fixes in `bug1_fixed.py` through `bug6_fixed.java` were based on the analysis in `../bug_snippets/ai_debug_log.md`. Each corrected function was checked with its original failing example plus additional normal, boundary, and invalid-input cases. Tests use the standard Python `unittest` module, Node.js built-in assertions, and a self-contained Java assertion runner. The six original snippet files were left untouched.

## Summary

| Original file | Fixed file | Defect addressed | Tests passed | Result |
| --- | --- | --- | ---: | --- |
| `bug1.py` | `bug1_fixed.py` | Off-by-one slice | 7 / 7 | PASS |
| `bug2.js` | `bug2_fixed.js` | Tax computed before discount | 6 / 6 | PASS |
| `bug3.java` | `bug3_fixed.java` | Integer division drops fractions | 6 / 6 | PASS |
| `bug4.py` | `bug4_fixed.py` | Shared mutable default argument | 6 / 6 | PASS |
| `bug5.js` | `bug5_fixed.js` | Counts order rows, not units | 6 / 6 | PASS |
| `bug6.java` | `bug6_fixed.java` | Maximum incorrectly starts at zero | 6 / 6 | PASS |
| **Total** | **6 fixed files** | | **37 / 37** | **PASS** |

## bug1.py → bug1_fixed.py

- **Original issue:** `len(activities) - count + 1` starts the slice one element too late.
- **Fix applied:** Changed the start index to `max(0, len(activities) - count)`; kept checks for zero, negative, and noninteger counts.
- **Original failing case:** `last_activities(["login", "search", "view", "logout"], 2)`.
- **Expected / actual after fix:** `['view', 'logout']` / `['view', 'logout']`.
- **Other tests:** zero count, count greater than list length, empty list, count of one, negative count rejected, noninteger count rejected.
- **Test results:** **7 passed, 0 failed.**

## bug2.js → bug2_fixed.js

- **Original issue:** Tax used the undiscounted `subtotal`.
- **Fix applied:** `const tax = discountedSubtotal * (taxPercent / 100);`. Kept two-decimal rounding; exported the function to permit automated testing.
- **Original failing case:** `invoiceTotal(100, 20, 10)`.
- **Expected / actual after fix:** `88` / `88`.
- **Other tests:** no discount (`110`), 100% discount (`0`), monetary rounding (`18.69`), zero subtotal (`0`), invalid discount rejected.
- **Test results:** **6 passed, 0 failed.**

## bug3.java → bug3_fixed.java

- **Original issue:** Integer division truncated the fractional portion of the mean before conversion to `double`.
- **Fix applied:** `return (double) total / ratings.length;`. Changed the accumulator from `int` to `long` to reduce risk of overflow for large sums. Renamed the Java public class to match the fixed filename.
- **Original failing case:** `averageRating(new int[]{4, 5})`.
- **Expected / actual after fix:** `4.5` / `4.5`.
- **Other tests:** one rating, equal ratings, two `Integer.MAX_VALUE` ratings (no `int` accumulation overflow), empty input rejected, null input rejected.
- **Test results:** **6 passed, 0 failed.**

## bug4.py → bug4_fixed.py

- **Original issue:** `report=[]` created a single mutable default list shared across calls.
- **Fix applied:** Changed the signature to `build_report(events, report=None)` and created an empty list when `report is None`. Explicitly supplied lists remain supported.
- **Original failing case:** Separate morning `['started', 'completed']` and evening `['failed']` reports.
- **Expected / actual after fix:** Morning `['started', 'completed']`; evening `['failed']` / exact match, in distinct list objects.
- **Other tests:** whitespace removal, explicit existing report, empty events, nonstring rejected, later calls do not mutate earlier reports.
- **Test results:** **6 passed, 0 failed.**

## bug5.js → bug5_fixed.js

- **Original issue:** `totals[productId] += 1` added one per order instead of the order's quantity.
- **Fix applied:** `totals[productId] += quantity;`. Also required positive safe-integer quantities and used a null-prototype working dictionary to avoid special-key collisions; returned a normal object and exported the function for tests.
- **Original failing case:** Orders for `plant-a` of 3 and 2 units and one `plant-b` unit.
- **Expected / actual after fix:** `{ 'plant-a': 5, 'plant-b': 1 }` / exact match.
- **Other tests:** empty orders, one order, fractional quantity rejected, missing quantity rejected, special product ID `__proto__` correctly counted.
- **Test results:** **6 passed, 0 failed.**

## bug6.java → bug6_fixed.java

- **Original issue:** Starting `highest` at zero returned zero incorrectly when every input temperature was negative.
- **Fix applied:** Set `int highest = readings[0];` after the existing empty/null check. Renamed the Java public class to match the fixed filename.
- **Original failing case:** `highestTemperature(new int[]{-7, -2, -5})`.
- **Expected / actual after fix:** `-2` / `-2`.
- **Other tests:** all positive readings, mixed signs, one negative reading, empty input rejected, null input rejected.
- **Test results:** **6 passed, 0 failed.**

## How to rerun the tests

Run these commands from the **repository root** (`holbertonschool-ai4devs/`). Python's standard library, Node.js, and a JDK (`javac` and `java`) are required.

### Python: 13 checks

```bash
python3 -m unittest discover -s smart_bug_bounty/bug_fixes/tests -p 'test_*.py' -v
```

Observed summary: `Ran 13 tests` followed by `OK`.

### JavaScript: 12 checks

```bash
node smart_bug_bounty/bug_fixes/tests/test_javascript_fixes.js
```

Observed summary: `JavaScript assertions passed: 12`.

### Java: 12 checks

```bash
mkdir -p /tmp/smart_bug_bounty_classes
javac -d /tmp/smart_bug_bounty_classes \
  smart_bug_bounty/bug_fixes/bug3_fixed.java \
  smart_bug_bounty/bug_fixes/bug6_fixed.java \
  smart_bug_bounty/bug_fixes/tests/FixValidation.java
java -cp /tmp/smart_bug_bounty_classes FixValidation
```

Observed summary: `Java assertions passed: 12`.

> On Windows, replace `/tmp/smart_bug_bounty_classes` with a local output folder such as `build` in both commands.

## Sample outputs of the repaired programs

| Program | Actual output (key result) |
| --- | --- |
| `python3 bug1_fixed.py` | `Last two activities: ['view', 'logout']` |
| `node bug2_fixed.js` | `Invoice total: 88` |
| `java bug3_fixed` | `Average: 4.5` |
| `python3 bug4_fixed.py` | `Morning report: ['started', 'completed']` and `Evening report: ['failed']` |
| `node bug5_fixed.js` | `Units sold: { 'plant-a': 5, 'plant-b': 1 }` |
| `java bug6_fixed` | `Highest temperature: -2` |

**Final assessment:** The six demonstrated defects are corrected. All 37 automated checks passed on Python 3.13.5, Node.js 22.16.0, and the installed Java runtime. This validation covers the listed cases; it is not a formal proof of correctness for every possible input.
