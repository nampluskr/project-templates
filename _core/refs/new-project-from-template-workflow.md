# New Project from Template Workflow

## 1. Purpose

This document defines the workflow for creating a new GitHub project repository from a template stored in `project-templates`.

Example:

```text
project-docs-template
→ new-docs-project
```

The same workflow applies to:

```text
project-docs-template
project-wiki-template
project-coding-template
```

## 2. Core Concept

`project-templates` is the source repository.

A new project is an independent GitHub repository created by copying one template into a new repository.

```text
project-templates repo = template source
new-docs-project repo = actual project
```

After creation, the new project is independent. Updating `project-templates` does not automatically update existing projects.

## 3. Prerequisites

Before creating a new project, confirm:

- `project-templates` exists on GitHub
- `project-templates` is cloned locally
- the target template exists under `templates/`
- a new GitHub repository name is chosen
- the new project type is known

Example local source:

```text
D:/projects/nampluskr/20_active/project-templates/
```

WSL equivalent:

```text
/mnt/d/projects/nampluskr/20_active/project-templates/
```

The exact local status folder may vary. The key point is that `project-templates` is the source repository.

## 4. Step 1: Create an Empty GitHub Repository

Create a new GitHub repository.

Example:

```text
nampluskr/new-docs-project
```

Recommended settings:

| Setting | Recommendation |
|---|---|
| Repository name | `new-docs-project` |
| Visibility | Private or Public depending on project |
| Initialize README | No |
| Add `.gitignore` | No |
| Add license | No |

Do not initialize files on GitHub if the template already includes `README.md`, `.gitignore`, `AGENTS.md`, and `CLAUDE.md`.

## 5. Step 2: Clone the Empty Repository

### Windows PowerShell

```powershell
cd D:\projects\nampluskr\00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

### WSL

```bash
cd /mnt/d/projects/nampluskr/00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

A new project can start in `00_review/` if it is still being tested or initialized. Move it to `20_active/` when it becomes a real working project.

## 6. Step 3: Copy the Template

### 6.1 WSL Recommended Method

```bash
rsync -av \
  /mnt/d/projects/nampluskr/20_active/project-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-docs-project/
```

### 6.2 Windows PowerShell Recommended Method

Use `robocopy` because it handles hidden files better than `Copy-Item`.

```powershell
robocopy `
  D:\projects\nampluskr\20_active\project-templates\templates\project-docs-template `
  D:\projects\nampluskr\00_review\new-docs-project `
  /E
```

## 7. Step 4: Verify the New Project Structure

For `project-docs-template`, the result should be:

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

For `project-wiki-template`, it should include:

```text
wiki/
```

For `project-coding-template`, it should include:

```text
pyproject.toml
requirements.txt
data/
src/
scripts/
notebooks/
tests/
configs/
experiments/
docs/
outputs/
```

## 8. Step 5: Initialize Project-Specific Content

After copying, update placeholder content.

Common placeholders:

```text
{{PROJECT_NAME}}
{{PROJECT_SLUG}}
{{PROJECT_DESCRIPTION}}
{{AUTHOR}}
```

Files to review:

```text
README.md
AGENTS.md
CLAUDE.md
_project/PROJECT.md
_project/PROJECT-TODO.md
docs/
```

## 9. Step 6: Open the New Project in VS Code

Open the new project root, not the `project-templates` root.

### Windows

```powershell
cd D:\projects\nampluskr\00_review\new-docs-project
code .
```

### WSL

```bash
cd /mnt/d/projects/nampluskr/00_review/new-docs-project
code .
```

## 10. Step 7: Use Codex for Initialization

Use a clear prompt that defines the project root and constraints.

Example:

```text
작업 대상은 현재 VS Code 루트인 new-docs-project 입니다.

이 프로젝트는 project-docs-template 기반의 문서 프로젝트입니다.

작업:
1. README.md를 new-docs-project 기준으로 초기화하세요.
2. _project/PROJECT.md를 작성하세요.
3. _project/PROJECT-TODO.md에 초기 작업 목록을 작성하세요.
4. docs 시작 문서를 확인하고, 없으면 생성하세요.

제약:
- 루트 폴더 구조를 변경하지 마세요.
- _project/ 내부 하위 구조를 변경하지 마세요.
- coding-template 전용 폴더인 src, scripts, notebooks, tests, configs, experiments 는 만들지 마세요.
```

## 11. Step 8: First Commit

```bash
git status
git add .
git commit -m "Initialize project from project-docs-template"
git push origin main
```

If the branch is not `main`:

```bash
git branch -M main
git push -u origin main
```

## 12. Step 9: Move the Project if Needed

If the project started under `00_review/` and becomes a real working project, move it to:

```text
20_active/
```

Example:

```text
D:/projects/nampluskr/00_review/new-docs-project
→ D:/projects/nampluskr/20_active/new-docs-project
```

Git remote settings remain valid after moving the local folder because they are stored inside the project’s `.git/config`.

After moving, verify:

```bash
git remote -v
git status
```

## 13. Template Update Policy

Existing projects are not automatically updated when the template changes.

If template updates should be applied later, do it selectively.

Potential update targets:

```text
AGENTS.md
CLAUDE.md
_project/rules/
_project/commands/
_project/docs/
```

Avoid blindly overwriting:

```text
README.md
_project/PROJECT.md
docs/
src/
notebooks/
```

These files are project-specific after creation.

## 14. Example Workflow Summary

```bash
cd /mnt/d/projects/nampluskr/00_review

git clone https://github.com/nampluskr/new-docs-project.git

rsync -av \
  /mnt/d/projects/nampluskr/20_active/project-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-docs-project/

cd new-docs-project
code .
```

Then use Codex to initialize project-specific content.

Finally:

```bash
git add .
git commit -m "Initialize project from project-docs-template"
git push origin main
```

## 15. Summary

New project creation follows this flow:

```text
1. Create empty GitHub repo
2. Clone repo locally
3. Copy selected template
4. Initialize placeholders
5. Open new project root in VS Code
6. Use Codex for project-specific setup
7. Commit and push
8. Move project from review to active when appropriate
```

The new project becomes independent after creation.