# Workflow Baseline

## Current IDE Setup
- **IDE:** VS Code
- **AI assistance:** GitHub Copilot (inline completions)
- **Formatting / linting:** Prettier, ESLint
- **Version control:** Git + GitHub, with the built-in VS Code Source Control panel
- **Terminal:** VS Code integrated terminal
- **Debugging:** VS Code built-in debugger and `console.log` / print statements
- **Testing:** Run manually from the terminal (e.g., `npm test` / `pytest`)

## Current Workflow
1. Pick up a task or issue from the GitHub repository.
2. Create a feature branch.
3. Write code with Copilot inline suggestions.
4. Write tests manually after the implementation.
5. Debug failures by reading logs and adding print statements.
6. Update documentation (README, comments) by hand.
7. Commit, push, and open a pull request.

## Pain Points
- **Too much manual test writing:** Unit tests are written by hand after the code, which is repetitive and often skipped under time pressure.
- **Repetitive documentation updates:** README and docstrings are updated manually and frequently fall out of sync with the code.
- **Slow debugging cycle:** Relying on print statements and rerunning tests means long loops to find root causes.
- **Context switching:** Moving between the editor, terminal, browser, and GitHub breaks focus.
- **Inconsistent commit messages:** Messages are written ad hoc, making history hard to scan.

## Productivity Metrics
| Metric | Baseline |
|---|---|
| Avg task completion time | ~90 min |
| Bug fix turnaround | ~2 h |
| Weekly commits | ~4 |
| Time spent writing tests (per task) | ~25 min |
| Time spent on documentation (per task) | ~15 min |

## How to Measure
- **Task completion time:** Track start and finish times for 5–10 tasks (e.g., with a timer or issue timestamps) and average them.
- **Bug fix turnaround:** Time from issue opened (or bug noticed) to fix merged.
- **Weekly commits:** `git log --since="1 week ago" --author="<your name>" --oneline | wc -l`

## Goal for Comparison
After integrating AI-assisted workflows, re-measure the same metrics and compare against this baseline.