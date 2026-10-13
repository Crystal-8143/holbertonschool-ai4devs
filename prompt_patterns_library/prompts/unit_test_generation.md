# Unit Test Generation Prompt Template

**Role**: Act as a software test engineer experienced with automated unit testing.

**Task**: Generate unit tests for the provided function. Cover normal behaviour, edge cases, and invalid inputs where relevant. Use the specified testing framework and do not assume that the tests have been executed.

**Input Placeholder**: 
- Programming language: [LANGUAGE]
- Function or source code: [CODE_BLOCK]
- Expected behaviour: [EXPECTED_BEHAVIOUR]
- Testing framework: [TESTING_FRAMEWORK]
- Relevant constraints: [CONSTRAINTS]

**Expected Output**: 
1. Runnable test code using the specified framework.
2. Tests for normal cases, edge cases, and invalid inputs.
3. A brief explanation of what each test verifies.
4. Any setup or execution instructions required.