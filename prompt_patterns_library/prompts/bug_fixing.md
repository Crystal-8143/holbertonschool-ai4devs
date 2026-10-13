# Bug Fixing Prompt Template

**Role**: Act as a software developer focused on fixing bugs with minimal changes.

**Task**: Investigate the difference between the expected and actual behaviour. Propose the smallest appropriate fix while preserving existing functionality.

**Input Placeholder**: 
- Programming language: [LANGUAGE]
- Relevant code: [CODE_BLOCK]
- Expected behaviour: [EXPECTED_BEHAVIOUR]
- Actual behaviour: [ACTUAL_BEHAVIOUR]
- Constraints: [CONSTRAINTS]

**Expected Output**: 
1. An explanation of the likely cause.
2. Corrected code.
3. A summary of the changes.
4. Suggested tests to verify the fix.