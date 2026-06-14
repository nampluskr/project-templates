# Project Templates Repository Design

## 1. Purpose

`project-templates` is a GitHub repository for managing reusable project workspace templates.

This repository is not a normal working project. It is the source repository for creating new project workspaces of different types.

The repository manages:

- common project operation files
- reusable project templates
- template usage guides
- template generation and validation scripts
- Codex / Claude Code working rules for maintaining the template repository

## 2. Repository Name

The final repository name is:

```text
project-templates
```

Recommended GitHub path:

```text
nampluskr/project-templates
```

The previous candidate name `project-workspace-templates` was rejected because it was longer than necessary. `project-templates` is shorter, easier to use in CLI commands, and still sufficiently descriptive.

## 3. Repository Role

`project-templates` has two roles.

| Role | Description |
|---|---|
| Template source repository | Stores reusable templates such as `project-docs-template`, `project-wiki-template`, and `project-coding-template` |
| Template management project | Has its own `AGENTS.md`, `CLAUDE.md`, `_project/`, guides, and scripts for maintaining the templates |

This distinction is important. The root-level files are for maintaining the `project-templates` repository itself. Files inside `templates/project-*-template/` are copied into newly created projects.

## 4. Final Root Structure

```text
project-templates/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _project/
├── shared/
├── templates/
├── guides/
└── scripts/
```

## 5. Directory Roles

| Path | Role |
|---|---|
| `README.md` | Public-facing explanation of the template repository |
| `AGENTS.md` | Codex working rules for maintaining this repository |
| `CLAUDE.md` | Claude Code working rules for maintaining this repository |
| `.gitignore` | Git ignore rules for this repository |
| `_project/` | Operation documents for the `project-templates` repository itself |
| `shared/` | Common source files reused by multiple templates |
| `templates/` | Template roots copied when creating new projects |
| `guides/` | Documentation for using and maintaining the templates |
| `scripts/` | Automation scripts for creation, synchronization, and validation |

## 6. Root-Level `AGENTS.md` and `CLAUDE.md`

The root-level files:

```text
project-templates/AGENTS.md
project-templates/CLAUDE.md
```

are for working on the template repository itself.

They should contain rules such as:

- how to modify `templates/`
- how to update `shared/`
- how to maintain `guides/`
- how to avoid confusing repository-level files with template files
- how to validate template root structures
- how to synchronize common `_project` files

They are not copied into new projects unless explicitly used as part of a template.

## 7. Template-Level `AGENTS.md` and `CLAUDE.md`

Each template contains its own `AGENTS.md` and `CLAUDE.md`.

Example:

```text
templates/project-docs-template/AGENTS.md
templates/project-docs-template/CLAUDE.md
```

These are template files. When a new project is created from a template, these files are copied into the new project root.

Example:

```text
templates/project-docs-template/AGENTS.md
→ new-docs-project/AGENTS.md
```

## 8. `_project/` Folder Distinction

There are two different `_project/` contexts.

```text
project-templates/
├── _project/
└── templates/
    ├── project-docs-template/
    │   └── _project/
    ├── project-wiki-template/
    │   └── _project/
    └── project-coding-template/
        └── _project/
```

| Path | Role |
|---|---|
| `project-templates/_project/` | Operation documents for the template repository itself |
| `templates/project-*/_project/` | Template operation folder copied into new projects |

The root `_project/` is not copied into new projects.

## 9. `shared/` Folder

The `shared/` folder stores common template source files.

Recommended structure:

```text
shared/
└── _project/
    ├── rules/
    ├── commands/
    └── docs/
```

This avoids maintaining duplicate versions of common rules, commands, and operation documents across all templates.

## 10. `templates/` Folder

The `templates/` folder contains the actual project templates.

```text
templates/
├── project-docs-template/
├── project-wiki-template/
└── project-coding-template/
```

Each template should be directly copyable into a new project repository.

## 11. `guides/` Folder

The `guides/` folder contains explanatory documents for users and AI agents.

Example guide files:

```text
guides/
├── project-templates-repository-design.md
├── project-template-types.md
├── shared-project-files-policy.md
├── new-project-from-template-workflow.md
└── codex-template-management-workflow.md
```

The folder was named `guides/`, not `template-guides/`, to avoid redundant naming with `templates/`.

## 12. `scripts/` Folder

The `scripts/` folder contains automation scripts.

Possible scripts:

```text
scripts/
├── create_project.py
├── sync_shared_project_files.py
├── validate_template.py
└── sync_agents.py
```

These scripts are for maintaining `project-templates` and creating new projects.

## 13. GitHub Repository Strategy

Only one template repository is created:

```text
nampluskr/project-templates
```

Separate repositories are not created for:

```text
project-docs-template
project-wiki-template
project-coding-template
```

Those are subdirectories inside `project-templates`.

This single-repository strategy reduces duplicated maintenance and keeps common rules synchronized.

## 14. Non-Goals

This repository does not manage the local D drive project status folders.

It does not define:

- `D:/projects/nampluskr/00_review/`
- `D:/projects/nampluskr/20_active/`
- `D:/projects/nampluskr/80_done/`
- `D:/projects/nampluskr/90_archive/`
- `D:/projects/nampluskr/99_deprecated/`

That topic is handled by the separate local D drive project management document.

## 15. Summary

`project-templates` is the single source repository for all reusable project workspace templates.

Core principles:

- one GitHub repository manages all templates
- root files manage the template repository itself
- template files are copied into new projects
- common `_project` files are managed through `shared/`
- template-specific differences are kept minimal
- `guides/` documents usage and management policies