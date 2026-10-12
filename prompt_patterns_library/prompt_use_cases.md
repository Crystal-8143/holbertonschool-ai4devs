# Prompt Use Cases
This document identifies common situations where prompt patterns can improve coding workflows. Each use case describes the goal, the input needed, and the expected output from the AI assistant.

## Code Quality
- **Refactoring Code**
  - **Goal**: Improve code readability, maintainability, and efficiency without changing its behaviour.
  - **Input**: An existing function or code block in a specified programming language.
  - **Output**: Refactored code with an explanation of the improvements.

- **Code Review**
    - **Goal**: Identify potential bugs, readability issues, and areas for improvement before merging code.
    - **Input**: A code file or pull request diff.
    - **Output**: A list of identified issues, suggested improvements, and corrected examples where appropriate.

- **Style Enforcement**
  - **Goal**: Apply consistent naming conventions, formatting, and coding standards. 
  - **Input**: A code block and the relevant style guidelines. 
  - **Output**: Revised code that follows the specified conventions, with a summary of the changes. 

## Debugging
- **Error Diagnosis**
  - **Goal**: Understand the cause of a runtime error or unexpected behaviour.
  - **Input**: The relevant code, error message, and steps to reproduce the problem.
  - **Output**: A likely explanation of the root cause and suggested steps to resolve it.

- **Bug Fixing**
    - **Goal**: Correct a specific bug while minimising changes to existing code.
    - **Input**: The code containing the bug, expected behaviour, and actual behaviour.
    - **Output**: A proposed fix with an explanation of why it works.

- **Performance Troubleshooting**
  - **Goal**: Identify potential performance bottlenecks in an application.
  - **Input**: Relevant code, performance measurements, and information about the workload.
  - **Output**: Potential bottlenecks, recommended optimisations, and suggestions for measuring the results.

## Documentation
- **Function Documentation**
  - **Goal**: Explain what a function does, its parameters, its return value, and possible errors.
  - **Input**: A function and its intended behaviour.
  - **Output**: Clear function documentation in the requested format, such as JSDoc or Python docstrings.

- **README Creation**
    - **Goal**: Help developers understand a project's purpose, setup, and usage.
    - **Input**: Project structure, dependencies, installation instructions, and key features.
    - **Output**: A structured README containing an overview, setup steps, usage examples, and other relevant information.

## Testing
- **Unit Test Generation**
  - **Goal**: Verify that individual functions behave as expected.
  - **Input**: A function, its expected behaviour, and the testing framework being used.
  - **Output**: Unit tests covering normal cases, edge cases, and invalid inputs.

- **Test Case Design**
    - **Goal**: Identify scenarios that should be tested to validate a feature or function.
    - **Input**: Feature requirements, expected outcomes, and known constraints.
    - **Output**: A list of test cases with inputs, expected results, and explanations of what each test verifies.

- **Test Failure Analysis**
  - **Goal**: Understand why an automated test fails and distinguish between implementation bugs and incorrect test expectations.
  - **Input**: The failing test, relevant source code, and test output.
  - **Output**: An explanation of the likely cause and recommended changes to the code or test.
