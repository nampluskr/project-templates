# Shared Project Files Policy

## 1. Purpose

This document defines what files are managed in `shared/`, how they are synced into templates, and what rules govern the sync process.

## 2. Shared Base Definition

The following files and folders are common to all three templates and are managed from `shared/` as the single source of truth.

```text
shared/
├── README.md
├── .gitignore
├── _project/
│   ├── PROJECT.md
│   ├── TASKS.md
│   ├── rules/
│   │   ├── markdown-style.md
│   │   └── python-style.md
│   └── commands/
│       └── sync.md
├── inbox/
├── sources/
├── outputs/
└── docs/
```

## 3. What Is NOT in Shared

`AGENTS.md` and `CLAUDE.md` are managed independently per template because their content differs by template type.

| File | Managed in |
|---|---|
| `AGENTS.md` | `templates/project-*/AGENTS.md` |
| `CLAUDE.md` | `templates/project-*/CLAUDE.md` |

Template-specific files (`wiki/`, `pyproject.toml`, etc.) are also not in `shared/`.

## 4. Sync Target

`scripts/sync_shared_project_files.py` copies shared files into all three templates.

| Source | Destination |
|---|---|
| `shared/README.md` | `templates/project-*/README.md` |
| `shared/.gitignore` | `templates/project-*/.gitignore` |
| `shared/_project/` | `templates/project-*/_project/` |

Empty folders (`inbox/`, `sources/`, `outputs/`, `docs/`) are represented by `.gitkeep` files and are not synced by script — they already exist in each template.

## 5. Sync Trigger

Run sync after any edit to files under `shared/`.

```bash
# Preview changes
python scripts/sync_shared_project_files.py --dry-run

# Apply changes
python scripts/sync_shared_project_files.py
```

## 6. Edit Rules

| Action | Correct Location |
|---|---|
| Edit common rules or commands | `shared/_project/rules/` or `shared/_project/commands/` |
| Edit README template | `shared/README.md` |
| Edit shared .gitignore | `shared/.gitignore` |
| Edit template-specific AGENTS.md | `templates/project-*/AGENTS.md` directly |
| Edit template-specific CLAUDE.md | `templates/project-*/CLAUDE.md` directly |

Never edit synced files directly inside `templates/project-*/` — changes will be overwritten on next sync.

## 7. After Sync

Review the changed files, then commit:

```bash
git add .
git commit -m "Sync shared files into templates"
git push origin main
```

## 8. New Project Creation

When creating a new project from a template, the `templates/project-*/` folder must already be in a synced state.

Copy the selected template using rsync (WSL) or robocopy (Windows):

```bash
rsync -av \
  /mnt/d/projects/nampluskr/20_active/project-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-project/
```

The new project receives the synced state at the moment of copying. It becomes independent after that point.