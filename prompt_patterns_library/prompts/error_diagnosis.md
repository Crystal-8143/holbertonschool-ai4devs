# Error Diagnosis Prompt Template

**Role**: Act as a debugging specialist who explains technical problems clearly.

**Task**: Investigate the provided error and identify its likely cause. Use the code, error message, and reproduction steps to explain what is happening. Do not assume a cause without supporting evidence.

**Input Placeholder**: 
- Programming language: [LANGUAGE]
- Relevant code: [CODE_BLOCK]
- Error message: [ERROR_MESSAGE]
- Steps to reproduce: [REPRODUCTION_STEPS]

**Expected Output**: 
1. The likely root cause of the error.
2. A clear explanation of why it occurs.
3. Suggested debugging steps.
4. A proposed fix, if enough information is available.