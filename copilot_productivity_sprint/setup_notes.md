# Setup Notes: Copilot Productivity Sprint

## 1. Environment Overview

| Item | Value |
|---|---|
| Operating System | `Windows 11` |
| Setup Date | `2026/11/4` |
| IDE | Visual Studio Code |
| AI Assistant | GitHub Copilot |
| GitHub Account | `Crystal-8143` |

## 2. Tool Versions

Run the following commands in the VS Code terminal and record the output.

| Tool | Command | Installed Version |
|---|---|---|
| VS Code | `code --version` | `1.144.1` |
| Git | `git --version` | `2.49.0.windows.1` |
| Node.js | `node --version` | `v22.16.0` |
| Python | `python --version` or `py --version` | `Python 3.13.4` |

## 3. IDE Installation

**Visual Studio Code**

1. Download VS Code from https://code.visualstudio.com/.
2. Install using the default installation options.
3. On Windows, enable the option to add VS Code to PATH.
4. Open VS Code.
5. Verify the installation using:

```bash
code --version
```

## 4. Extensions Installed

List installed extensions and their versions using:

```bash
code --list-extensions --show-versions
```

Record the relevant extensions below.

| Extension | Extension ID | Version | Purpose |
|---|---|---|---|
| GitHub Copilot | `GitHub.copilot` | `1.388.0 (deprecated)` | AI-powered inline code suggestions |
| GitHub Copilot Chat | `GitHub.copilot-chat` | `0.72.0` | AI chat, code explanations and generation |

## 5. GitHub Copilot Installation and Configuration

**Installation steps:**

1. Visit https://github.com/features/copilot.
2. Sign in using a GitHub account and obtain Copilot access (Free, Pro or eligible GitHub Education access).
3. Open Visual Studio Code.
4. Open Extensions using `Ctrl + Shift + X`.
5. Search for GitHub Copilot.
6. Install the official GitHub Copilot extension. Install Copilot Chat separately if it is not included automatically.
7. Sign in with GitHub when prompted.
8. Authorise VS Code through the browser.
9. Confirm that Copilot is active in VS Code.

**Configuration:**

| Setting | Configuration |
|---|---|
| AI assistant | GitHub Copilot |
| Inline code suggestions | Enabled |
| Copilot Chat | Enabled |
| Authentication | GitHub account |
| Language support | `default` |

## 6. Copilot Functionality Test

Verify that both inline suggestions and Copilot Chat work correctly.

**Test 1: Inline code suggestions**

1. Create a new file called `test.py`.
2. Enter the following comment:

```python
# Function that reverses a string
```

3. Wait for Copilot to generate a suggestion.
4. Press `Tab` to accept the suggestion.
5. Confirm that code is generated successfully.

**Test 2: Copilot Chat**

1. Open Copilot Chat in VS Code.
2. Enter the following prompt:

"Explain what this function does and identify any potential improvements."

3. Confirm that Copilot returns a relevant response.

**Expected outcome:** Both inline code completion and Copilot Chat operate successfully.