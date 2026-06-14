# New Project from Template Workflow

## 1. Purpose

This document defines the workflow for creating a new GitHub repository from a template in `project-templates`.

## 2. Core Concept

```text
project-templates/templates/project-docs-template/  (source)
    ↓ copy
nampluskr/new-docs-project  (independent GitHub repo)
```

After creation, the new project is fully independent. Updating `project-templates` does not affect existing projects.

## 3. Prerequisites

- `project-templates` cloned locally at `D:/projects/nampluskr/20_active/project-templates/`
- Templates are in a synced state (run `sync_shared_project_files.py` if unsure)
- New GitHub repository name is chosen
- Template type is decided

## 4. Step 1: Create Empty GitHub Repository

Create a new repository on GitHub with no initialization (no README, no .gitignore, no license).

Recommended settings:

| Setting | Value |
|---|---|
| Repository name | e.g. `new-docs-project` |
| Visibility | Private or Public |
| Initialize README | No |

## 5. Step 2: Clone the Empty Repository

### WSL

```bash
cd /mnt/d/projects/nampluskr/00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

### Windows PowerShell

```powershell
cd D:\projects\nampluskr\00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

Start in `00_review/`. Move to `20_active/` when the project becomes a real working project.

## 6. Step 3: Copy the Template

### WSL (recommended)

```bash
rsync -av \
  /mnt/d/projects/nampluskr/20_active/project-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-docs-project/
```

### Windows PowerShell

```powershell
robocopy `
  D:\projects\nampluskr\20_active\project-templates\templates\project-docs-template `
  D:\projects\nampluskr\00_review\new-docs-project `
  /E
```

Replace `project-docs-template` with `project-wiki-template` or `project-coding-template` as needed.

## 7. Step 4: Verify the New Project Structure

After copying, confirm the expected structure is present.

For `project-docs-template`:

```text
new-docs-project/
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

For `project-wiki-template`, also check:

```text
└── wiki/
```

For `project-coding-template`, also check:

```text
├── pyproject.toml
├── requirements.txt
├── data/
├── src/
├── scripts/
├── notebooks/
├── tests/
├── configs/
└── experiments/
```

## 8. Step 5: Initialize Project-Specific Content

Update placeholder values:

```text
{{PROJECT_NAME}}
{{PROJECT_SLUG}}
{{PROJECT_DESCRIPTION}}
{{AUTHOR}}
```

Files to update:

```text
README.md
AGENTS.md
CLAUDE.md
_project/PROJECT.md
_project/TASKS.md
```

## 9. Step 6: Open in VS Code

Open the new project root, not `project-templates`.

```bash
cd /mnt/d/projects/nampluskr/00_review/new-docs-project
code .
```

## 10. Step 7: First Commit

```bash
git add .
git commit -m "Initialize project from project-docs-template"
git branch -M main
git push -u origin main
```

## 11. Step 8: Move Project When Ready

When the project moves from review to active:

```text
D:/projects/nampluskr/00_review/new-docs-project
→ D:/projects/nampluskr/20_active/new-docs-project
```

Git remote settings remain valid after moving.

Verify after move:

```bash
git remote -v
git status
```

## 12. Template Update Policy

Existing projects are not updated when `project-templates` changes.

If a template update needs to be applied to an existing project, do it selectively:

Safe to update:

```text
AGENTS.md
CLAUDE.md
_project/rules/
_project/commands/
```

Do not blindly overwrite:

```text
README.md
_project/PROJECT.md
_project/TASKS.md
docs/
src/
```

These are project-specific after creation.