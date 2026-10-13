# Unit Test Generation Prompt Template

**Role:** Act as a software test engineer experienced with the specified programming language and testing framework.

**Task:** Create unit tests for the supplied function or module. Cover normal behaviour, boundary conditions, and invalid inputs where relevant. Do not claim that generated tests have been run.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Function or source code: [CODE_BLOCK]
- Expected behaviour: [EXPECTED_BEHAVIOUR]
- Testing framework: [TESTING_FRAMEWORK]
- Existing tests or project setup: [TEST_CONTEXT]
- Constraints: [CONSTRAINTS]

**Expected Output:**
1. **Test code:** Provide the tests in a fenced code block labelled with [LANGUAGE].
2. **Coverage summary:** Use a numbered list to identify the normal cases, edge cases, and invalid-input cases covered.
3. **Expected results:** For each test, state what result or behaviour it verifies.
4. **Execution instructions:** Provide the command needed to run the tests, if it can be determined from the supplied context.
5. **Assumptions:** List assumptions about the function or test environment.
