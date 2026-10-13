# Test Failure Analysis Prompt Template

**Role:** Act as a debugging engineer who specialises in diagnosing automated test failures.

**Task:** Compare the test's expected result with the actual result. Examine the test, implementation, and error output to identify the likely cause. Do not assume that the implementation or the test is correct without checking the requirements.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Testing framework: [TESTING_FRAMEWORK]
- Test code: [TEST_CODE]
- Relevant implementation: [IMPLEMENTATION_CODE]
- Test output or error message: [TEST_OUTPUT]
- Intended behaviour or requirements: [EXPECTED_BEHAVIOUR]

**Expected Output:**
1. **Failure summary:** State which test failed and how the actual result differs from the expected result.
2. **Likely cause:** Explain the most likely cause and the evidence supporting it.
3. **Recommended correction:** Explain whether the implementation, test, or requirements may need to change. Include a code example in a fenced code block when appropriate.
4. **Regression tests:** Provide a numbered list of additional tests with their expected results.
5. **Verification steps:** Give the command or steps to rerun the relevant tests, if known.
6. **Uncertainty:** List any missing information needed to confirm the diagnosis.
