# Project Template Types

## 1. Purpose

This document defines the three project template types managed in the `project-templates` repository.

```text
templates/
├── project-docs-template/
├── project-wiki-template/
└── project-coding-template/
```

Each template defines only the root-level workspace structure.

## 2. Inheritance Model

All three templates share a common base defined in `shared/`.

```text
shared/  (common base)
    |
    +--[wiki/ 추가]-----------> project-wiki-template
    |
    +--[코딩 도구 추가]---------> project-coding-template
```

`project-docs-template` is the shared base with no additions.

## 3. Shared Base (common to all templates)

```text
README.md
.gitignore
_project/
inbox/
sources/
outputs/
docs/
```

`AGENTS.md` and `CLAUDE.md` are NOT shared. Each template manages its own.

## 4. Template Overview

| Template | Adds on top of shared base | Main Output |
|---|---|---|
| `project-docs-template` | Nothing | Markdown docs, guides, manuals |
| `project-wiki-template` | `wiki/` | Wiki notes and structured docs |
| `project-coding-template` | Coding tools (see below) | Source code, notebooks, experiment outputs, docs |

## 5. Template Selection Guide

| Project Situation | Recommended Template |
|---|---|
| Write a technical guide or manual | `project-docs-template` |
| Write a setup or process document | `project-docs-template` |
| Lightweight Jupyter Book project | `project-docs-template` |
| Build long-term knowledge notes | `project-wiki-template` |
| Research documentation with wiki | `project-wiki-template` |
| Obsidian-style wiki + final docs | `project-wiki-template` |
| Python scripts, notebooks, tests | `project-coding-template` |
| PyTorch deep learning project | `project-coding-template` |
| NumPy numerical analysis project | `project-coding-template` |
| Experiment management | `project-coding-template` |

## 6. `project-docs-template`

### Root Structure

```text
project-docs-template/
├── README.md               # shared
├── AGENTS.md               # docs-specific
├── CLAUDE.md               # docs-specific
├── .gitignore              # shared
├── _project/               # shared
├── inbox/                  # shared
├── sources/                # shared
├── docs/                   # shared
└── outputs/                # shared
```

### Information Flow

```text
inbox/ → sources/ → docs/ → outputs/
```

### Example Projects

```text
wsl-cuda-setup-guide
vscode-codex-usage-guide
jupyter-book-build-guide
github-submodule-guide
```

## 7. `project-wiki-template`

### Root Structure

```text
project-wiki-template/
├── README.md               # shared
├── AGENTS.md               # wiki-specific
├── CLAUDE.md               # wiki-specific
├── .gitignore              # shared
├── _project/               # shared
├── inbox/                  # shared
├── sources/                # shared
├── wiki/                   # wiki-specific
├── docs/                   # shared
└── outputs/                # shared
```

### Information Flow

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

### Example Projects

```text
display-anomaly-detection-wiki
deep-learning-from-scratch-book
oled-color-science-notes
papers-to-book-workspace
```

## 8. `project-coding-template`

### Root Structure

```text
project-coding-template/
├── README.md               # shared
├── AGENTS.md               # coding-specific
├── CLAUDE.md               # coding-specific
├── .gitignore              # shared
├── pyproject.toml          # coding-specific
├── requirements.txt        # coding-specific
├── _project/               # shared
├── inbox/                  # shared
├── sources/                # shared
├── data/                   # coding-specific
├── src/                    # coding-specific
├── scripts/                # coding-specific
├── notebooks/              # coding-specific
├── tests/                  # coding-specific
├── configs/                # coding-specific
├── experiments/            # coding-specific
├── docs/                   # shared
└── outputs/                # shared
```

### Internal Structure Policy

The template defines only the root-level folders above.
Internal structure of `src/` is decided per project.

### Example Projects

```text
mnist-from-scratch-mlp
oled-anomaly-detection
gan-training-framework
numpy-numerical-analysis
pytorch-classification-template
```

## 9. Feature Comparison

| Feature | Docs | Wiki | Coding |
|---|:---:|:---:|:---:|
| `README.md` `.gitignore` `_project/` | O | O | O |
| `inbox/` `sources/` `outputs/` `docs/` | O | O | O |
| `wiki/` | - | O | - |
| `pyproject.toml` `requirements.txt` | - | - | O |
| `data/` `src/` `scripts/` | - | - | O |
| `notebooks/` `tests/` `configs/` `experiments/` | - | - | O |