# Test Failure Analysis Prompt Template

**Role**: Act as a debugging engineer who specializes in diagnosing automated test failures.

**Task**: Compare the failing test's expected result with the actual result. Examine the test and implementation to identify the likely cause without assuming that either one is necessarily correct.

**Input Placeholder**: 
- Programming language: [LANGUAGE]
- Testing framework: [TESTING_FRAMEWORK]
- Test code: [TEST_CODE]
- Relevant implementation: [IMPLEMENTATION_CODE]
- Test output or error message: [TEST_OUTPUT]
- Intended behaviour: [EXPECTED_BEHAVIOUR]

**Expected Output**: 
1. A summary of the failure.
2. The likely cause, supported by the available evidence.
3. Recommended changes to the implementation or test.
4. Additional tests to help prevent the issue from recurring.