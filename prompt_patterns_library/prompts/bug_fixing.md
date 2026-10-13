# Bug Fixing Prompt Template

**Role:** Act as a software developer who fixes bugs with minimal, focused changes.

**Task:** Compare the expected and actual behaviour, identify the likely cause, and propose the smallest appropriate fix while preserving unrelated functionality.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Relevant code: [CODE_BLOCK]
- Expected behaviour: [EXPECTED_BEHAVIOUR]
- Actual behaviour: [ACTUAL_BEHAVIOUR]
- Constraints or related requirements: [CONSTRAINTS]

**Expected Output:**
1. **Cause:** Explain the likely cause of the bug and the evidence supporting the diagnosis.
2. **Corrected code:** Provide the relevant corrected code in a fenced code block labelled with [LANGUAGE].
3. **Change summary:** List the changes and explain how they address the bug.
4. **Verification tests:** Provide a numbered list of tests, each with the input or action and expected result.
5. **Assumptions:** Identify any assumptions or missing information.
