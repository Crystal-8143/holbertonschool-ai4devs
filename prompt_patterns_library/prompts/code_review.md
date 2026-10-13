# Code Review Prompt Template

**Role:** Act as a software developer reviewing code for correctness, readability, security, and maintainability.

**Task:** Review the supplied code against the requirements. Identify concrete issues, prioritise them by severity, and explain each finding. Do not report speculative issues as confirmed bugs.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Source code or pull request diff: [CODE_BLOCK]
- Requirements: [REQUIREMENTS]
- Relevant context: [CONTEXT]

**Expected Output:**
1. **Review findings:** Use a numbered list. For each finding, include severity (High, Medium, or Low), the relevant code or location, the issue, and its impact.
2. **Suggested fixes:** Provide a specific recommendation for each finding.
3. **Example changes:** Include revised code in a fenced code block when useful.
4. **Questions or limitations:** List information needed to confirm uncertain findings, or state "None" if no further information is needed.
