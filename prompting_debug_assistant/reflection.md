# Reflection on AI-Assisted Debugging

## Introduction
For this exercise, I used AI (ChatGPT) to help identify and fix 6 different bugs across 3 different coding languages (Python, JavaScript, and Ruby). These bugs included a range of common errors from snippets of code: 
- Syntax errors
- Runtime issues
- Logical errors
- Off-by-one error
- Data type problem

I first asked the AI to explain what was wrong and to suggest a fix, then applied the the suggestions to the seperate fixed files to test the results. This helped me understand how AI can be useful during debugging but still requires the developer to verify the suggested solution.

## AI Strengths
The AI is extremely fast at identifying and finding solutions to the problem. The easiest bugs that were identified were the syntax errors and the off-by-one error. For example, `bug1.py` was only missing a colon in the Python function definition, and changing `i <= item.length` to `i < items.length` to fix the JavaScript loop in `bug4.js`.

The AI also handled the percentage calculation in `bug3.js` well. It correctly identified that the discount was being treated as a dollar amount instead of a percentage and suggested calculating the percentage before subtracting it.

Overall, AI made the debugging process faster because I could get an explanation and possible solution quickly instead of starting from scratch.

## AI Weaknesses
AI is known to have poor handling of complex architecture and low to medium contextual code awareness. The harder bugs required more attention to the intended behaviour of the program. In the case of `bug2.py`, the AI had to decide what should happen when a user cannot be found. The important part was not just finding an error but understanding that the function should safely return `None`.

In bug6.py, the code worked, but it used `> 50` when the requirement was that a score of 50 or higher should pass. This is a logical boundary issue that can be easy to miss if only normal examples are tested.

## Human Role
I would not completely trust an AI-generated fix without testing it. AI can identify patterns quickly, but it does not automatically know whether its interpretation matches the requirements of a particular project.

Human intuition was important when deciding what the code was supposed to do and checking whether the proposed fix actually matched that behaviour. Running the corrections and comparing the results with the original results was an important part of the process.

While the applied solutions from the AI were successful, therefore I didn't need to do extra manual changes, I still needed to make the final decision about whether each fix was correct.

## Conclusion
This exercise showed me that AI can be a useful debugging assistant, especially for identifying common programming mistakes and explaining unfamiliar errors. It can make debugging faster and provide a useful starting point when I am stuck.

However, AI **Should Not** replace manual testing or personal understading of the code. In the real-world AI should be used as a tool to suggest possible causes and solutions and not replace human reasoning, project requirements, tests and documentation to verify results. The developer remains responsible for deciding whether the solution is actually correct.