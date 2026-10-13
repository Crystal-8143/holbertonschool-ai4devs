# Function Documentation Prompt Template

**Role:** Act as a technical writer experienced in documenting software functions accurately and clearly.

**Task:** Document the supplied function so another developer can understand its purpose, parameters, return value, errors, and usage. Do not invent behaviour that is not supported by the code or context.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Function code: [FUNCTION_CODE]
- Intended behaviour or additional context: [FUNCTION_CONTEXT]
- Documentation format: [DOCUMENTATION_FORMAT]

**Expected Output:**
1. **Function documentation:** Provide documentation in the requested format, such as JSDoc or Python docstrings, in a fenced code block.
2. **Parameters:** Describe each parameter, including its type when known and its purpose.
3. **Return value:** Describe the return value and its type when known.
4. **Errors and edge cases:** List relevant exceptions, errors, or edge cases. If none are evident, say that none were identified from the supplied information.
5. **Usage example:** Provide a short example in a fenced code block when appropriate.
