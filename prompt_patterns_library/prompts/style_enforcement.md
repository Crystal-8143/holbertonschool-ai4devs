# Style Enforcement Prompt Template

**Role:** Act as a code quality specialist who follows the supplied programming-language and project style guidelines.

**Task:** Revise the supplied code to follow the specified naming, formatting, and style rules without changing its behaviour or adding unrelated features.

**Input Placeholder:**
- Programming language: [LANGUAGE]
- Source code: [CODE_BLOCK]
- Style guide or rules: [STYLE_GUIDELINES]
- Constraints: [CONSTRAINTS]

**Expected Output:**
1. **Revised code:** Provide the complete updated code in a fenced code block labelled with [LANGUAGE].
2. **Style changes:** List each important change and the rule it follows.
3. **Behaviour preservation:** State whether any behaviour was intentionally changed. If none, state that the goal was to preserve behaviour.
4. **Unresolved rules:** List any rules that could not be applied and explain why, or state "None".
