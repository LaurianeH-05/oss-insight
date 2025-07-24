# OSS Insight 🌐

OSS Insight is a tool for new developers looking to contribute meaningfully to open source. It scans GitHub repositories and suggests high-impact contributions based on commit history, open issues, and code structure.

> ⚠️ This project is in active development.

## 🎯 Goals

- 🧠 Parse a public GitHub repo and identify:
  - Starter-friendly issues
  - Stale but important files
  - Contribution hotspots (modules under heavy change)
- 🛠️ Provide command-line suggestions for:
  - First contributions
  - New tests or docstrings
  - Feature improvements

## 🛠️ Tech Stack

- **Language:** Python
- **GitHub API:** For repo metadata and issues
- **CLI Tool:** Typer / Rich (planned)
- **Future:** React UI for visual insights (Phase 2)
