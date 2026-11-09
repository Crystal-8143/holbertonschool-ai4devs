# AI Assistant Configuration

## Overview
GitHub Copilot is configured at the project level so every contributor gets the same language rules and AI workflows.

| File | Purpose |
|---|---|
| `.copilot-settings.yaml` | Readable source of truth for language rules and workflows |
| `.vscode/settings.json` | Enforced VS Code and Copilot settings that implement the YAML |

> Copy both to your project root (`.copilot-settings.yaml` at the root, `.vscode/` at the root) when using them in a real project. VS Code reads only `.vscode/settings.json` automatically; the YAML is documentation and team convention, not a file Copilot reads on its own.

## Setup Steps
1. Install VS Code extensions: **GitHub Copilot**, **GitHub Copilot Chat**, **Prettier**, **ESLint**, **Black Formatter**.
2. Sign in to GitHub from VS Code and confirm your Copilot subscription is active.
3. Open the project folder so `.vscode/settings.json` is applied as workspace settings.
4. Run `npm install` and `pip install black pytest` for the formatters and test tools.
5. Verify: open a `.py` file, type a function signature, and check that Copilot suggests type-hinted code.

## Language-Specific Rules
| Language | Style | Rules |
|---|---|---|
| Python | Black | 88 columns, type hints required, Google-style docstrings, pytest |
| JavaScript | Airbnb | Semicolons, single quotes, const/let, async/await, Jest |
| Markdown | n/a | Sentence-case headings, no hard wrapping |

Formatting is applied on save; Copilot generation rules are set in `github.copilot.chat.codeGeneration.instructions`.

## Specialized AI Workflows

### 1. Code Review (primary)
- **Trigger:** select code, then right-click, then **Copilot > Review** (or run it from the Source Control panel).
- **Focus areas:** security, performance, readability, error handling.
- **Output:** findings labeled blocker, major, minor or nit, each with a suggested fix.
- **Config:** `github.copilot.chat.reviewSelection.instructions`.

### 2. Test Generation
- **Trigger:** select a function, then `/tests` in Copilot Chat.
- **Behavior:** covers happy path, edge cases and error cases, using pytest or Jest.
- **Config:** `github.copilot.chat.testGeneration.instructions`.

### 3. Commit Messages
- **Trigger:** click the sparkle icon in the Source Control message box.
- **Behavior:** produces Conventional Commits messages.
- **Config:** `github.copilot.chat.commitMessageGeneration.instructions`.

### 4. Documentation Generation
- **Trigger:** select code, then `/doc` in Copilot Chat.
- **Behavior:** concise docstrings in the project style, with a usage example.

## Privacy and Safety
- Copilot is disabled for plaintext files.
- Secrets (`.env`, `*.pem`, `secrets/**`) must never be pasted into chat. Consider a Copilot content exclusion rule in your GitHub org or repo settings.
- Always review AI output before committing.

## Addressing Baseline Pain Points
| Pain point (from `workflow_baseline.md`) | Configured solution |
|---|---|
| Too much manual test writing | Test generation workflow |
| Repetitive documentation updates | Documentation generation workflow |
| Slow debugging cycle | Review workflow flags error-handling issues early |
| Inconsistent commit messages | Conventional Commits generation |