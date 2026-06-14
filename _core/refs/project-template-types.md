# Project Template Types

## 1. Purpose

This document defines the project template types managed in the `project-templates` repository.

The repository contains three primary template types:

```text
project-docs-template
project-wiki-template
project-coding-template
```

Each template defines only the root-level workspace structure. Detailed internal structures, such as `src/` package layouts or `_project/` subfolder contents, are handled by guides and project-specific decisions.

## 2. Template List

```text
templates/
├── project-docs-template/
├── project-wiki-template/
└── project-coding-template/
```

| Template | Main Purpose | Main Output |
|---|---|---|
| `project-docs-template` | Simple documentation project | Markdown docs, guides, manuals |
| `project-wiki-template` | Documentation plus wiki knowledge base | Wiki notes and structured docs |
| `project-coding-template` | Python coding, experiments, notebooks, and documentation | Source code, notebooks, experiment outputs, docs |

## 3. Template Selection Guide

| Project Situation | Recommended Template |
|---|---|
| Write a technical guide or manual | `project-docs-template` |
| Build long-term knowledge notes and final documents | `project-wiki-template` |
| Manage Python scripts, notebooks, tests, and docs together | `project-coding-template` |
| Create a Jupyter Book style document project without wiki | `project-docs-template` |
| Manage Obsidian-style wiki notes and docs | `project-wiki-template` |
| Build a PyTorch deep learning project | `project-coding-template` |
| Build a NumPy numerical analysis project | `project-coding-template` |
| Validate algorithms using scripts and notebooks | `project-coding-template` |

## 4. Common Template Principle

All templates should follow these principles:

- define only root-level folders and files
- do not force detailed internal structure too early
- include `README.md`, `AGENTS.md`, `CLAUDE.md`, `.gitignore`, and `_project/`
- provide `docs/` as the final documentation location
- use `inbox/`, `sources/`, and `outputs/` when applicable
- keep template-specific additions minimal

## 5. `project-docs-template`

### 5.1 Purpose

`project-docs-template` is the simplest documentation-oriented project template.

It is suitable for:

- usage guides
- technical manuals
- project notes
- setup documents
- process documentation
- lightweight Jupyter Book projects

### 5.2 Root Structure

```text
project-docs-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _project/
├── inbox/
├── sources/
├── docs/
└── outputs/
```

### 5.3 Directory Roles

| Path | Role |
|---|---|
| `README.md` | GitHub-facing project overview |
| `AGENTS.md` | Codex project instructions |
| `CLAUDE.md` | Claude Code project instructions |
| `.gitignore` | Git ignore rules |
| `_project/` | Project operation documents |
| `inbox/` | Temporary unorganized input material |
| `sources/` | Organized source material |
| `docs/` | Final documentation |
| `outputs/` | Generated outputs, exports, or build results |

### 5.4 Example Projects

```text
wsl-cuda-setup-guide
vscode-codex-usage-guide
dex-coding-workflow-guide
github-submodule-guide
jupyter-book-build-guide
```

## 6. `project-wiki-template`

### 6.1 Purpose

`project-wiki-template` is for projects that need both a knowledge base and final documentation.

It is suitable for:

- long-term study notes
- book writing
- research documentation
- paper-to-doc workflows
- Obsidian-compatible wiki systems
- docs + wiki projects based on AGENTS.md v2.1 style

### 6.2 Root Structure

```text
project-wiki-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _project/
├── inbox/
├── sources/
├── wiki/
├── docs/
└── outputs/
```

### 6.3 Directory Roles

| Path | Role |
|---|---|
| `wiki/` | Working knowledge base, concepts, notes, references |
| `docs/` | Final structured documentation |
| `sources/` | Organized source materials |
| `inbox/` | Temporary unprocessed input |
| `outputs/` | Build outputs or exported documents |

### 6.4 Information Flow

```text
inbox/
→ sources/
→ wiki/
→ docs/
→ outputs/
```

### 6.5 Example Projects

```text
display-anomaly-detection-wiki
deep-learning-from-scratch-book
oled-color-science-notes
computer-vision-study-wiki
papers-to-book-workspace
```

## 7. `project-coding-template`

### 7.1 Purpose

`project-coding-template` is for code-centric projects that still need structured documentation.

It is suitable for:

- PyTorch deep learning projects
- NumPy numerical analysis projects
- MATLAB-to-Python algorithm validation
- experiment management
- notebook-based analysis
- testable Python packages
- coding projects with documentation

### 7.2 Root Structure

```text
project-coding-template/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── _project/
├── inbox/
├── sources/
├── data/
├── src/
├── scripts/
├── notebooks/
├── tests/
├── configs/
├── experiments/
├── docs/
└── outputs/
```

### 7.3 Directory Roles

| Path | Role |
|---|---|
| `pyproject.toml` | Python project configuration |
| `requirements.txt` | Basic dependency list |
| `data/` | Data location or data instructions |
| `src/` | Source code root |
| `scripts/` | Runnable scripts |
| `notebooks/` | Jupyter notebooks |
| `tests/` | Test code |
| `configs/` | Configuration files |
| `experiments/` | Experiment records and run metadata |
| `docs/` | Project documentation |
| `outputs/` | Figures, reports, checkpoints, predictions, exports |

### 7.4 Internal Structure Policy

The template defines only:

```text
src/
```

It does not force a specific internal package structure.

PyTorch-specific and NumPy-specific examples should be described in separate guide documents or project-specific documentation.

### 7.5 Example Projects

```text
mnist-from-scratch-mlp
oled-anomaly-detection
gan-training-framework
matlab-to-python-validation
numpy-numerical-analysis
pytorch-classification-template
```

## 8. Template Comparison

| Feature | Docs | Wiki | Coding |
|---|---:|---:|---:|
| `docs/` | Required | Required | Required |
| `wiki/` | No | Required | Optional |
| `src/` | No | Optional | Required |
| `notebooks/` | No | Optional | Required |
| `tests/` | No | No | Required |
| `data/` | No | No | Required |
| `outputs/` | Recommended | Recommended | Required |
| Best for manuals | Yes | Possible | Possible |
| Best for knowledge bases | Limited | Yes | Possible |
| Best for Python development | No | Limited | Yes |

## 9. Summary

Use:

- `project-docs-template` for simple documentation
- `project-wiki-template` for knowledge accumulation plus final docs
- `project-coding-template` for Python source code, notebooks, experiments, and docs

Keep root structures stable and simple. Move detailed internal structures to guides or project-specific decisions.