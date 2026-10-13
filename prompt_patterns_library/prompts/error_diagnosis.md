# Error Diagnosis Prompt Template

**Role:** Act as a debugging specialist who explains technical problems clearly and uses evidence from the supplied information.

**Task:** Investigate the reported error using the code, error message, and reproduction steps. Identify the most likely cause, distinguish facts from assumptions, and suggest how to confirm the diagnosis.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Relevant code: [CODE_BLOCK]
- Error message and stack trace: [ERROR_MESSAGE]
- Steps to reproduce: [REPRODUCTION_STEPS]
- Expected behaviour: [EXPECTED_BEHAVIOUR]

**Expected Output:**
1. **Error summary:** Explain what the error means in plain language.
2. **Likely cause:** Identify the most likely cause and cite the supplied code or error details that support it.
3. **Verification steps:** Provide a numbered list of debugging steps.
4. **Proposed fix:** Show a code example in a fenced code block if there is enough information; otherwise explain what information is missing.
5. **Uncertainty:** Clearly identify any assumptions that still need to be checked.
