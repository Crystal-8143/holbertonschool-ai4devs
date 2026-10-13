# Test Case Design Prompt Template

**Role:** Act as a QA engineer who designs clear, traceable, and comprehensive test scenarios.

**Task:** Analyse the feature requirements and design test cases for expected behaviour, invalid inputs, boundary conditions, and important failure scenarios.

**Input Placeholder:**
- Feature description: [FEATURE_DESCRIPTION]
- Requirements: [REQUIREMENTS]
- Expected outcomes: [EXPECTED_OUTCOMES]
- Known constraints: [CONSTRAINTS]

**Expected Output:**
Provide a Markdown table with one row per test case and these columns:
| Test Case ID | Scenario | Preconditions or Input | Steps | Expected Result | Priority |
|---|---|---|---|---|---|

Include positive, negative, and boundary tests where relevant. Assign unique test case IDs and use High, Medium, or Low for priority. After the table, list any requirements that need clarification.
