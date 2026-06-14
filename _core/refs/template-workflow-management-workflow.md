# Codex Template Management Workflow

## 1. Purpose

This document defines how to use Codex to manage the `project-templates` repository.

It covers:

- which VS Code root to open
- how to distinguish repository-level work from template-level work
- how to write safe Codex prompts
- how to modify templates
- how to update shared files
- how to validate changes

## 2. Working Root Principle

When maintaining the template repository, open the `project-templates` root in VS Code.

Example:

```text
D:/projects/nampluskr/20_active/project-templates/
```

WSL:

```text
/mnt/d/projects/nampluskr/20_active/project-templates/
```

Codex should see this as the workspace root.

Do not open only `templates/project-docs-template/` unless intentionally working on that template in isolation.

## 3. Repository-Level vs Template-Level Work

There are two main contexts.

| Context | Work Root | Purpose |
|---|---|---|
| Repository-level work | `project-templates/` | Maintain the template repository |
| Generated project work | `new-project/` | Work on a project created from a template |

This document is about repository-level work.

## 4. Important Path Distinctions

```text
project-templates/
├── AGENTS.md
├── CLAUDE.md
├── _project/
├── shared/
├── templates/
├── guides/
└── scripts/
```

| Path | Codex Meaning |
|---|---|
| `AGENTS.md` | Codex instructions for maintaining `project-templates` itself |
| `CLAUDE.md` | Claude Code instructions for maintaining `project-templates` itself |
| `_project/` | Operation documents for the template repository itself |
| `shared/` | Common source files reused by templates |
| `templates/` | Copyable template roots |
| `guides/` | Human and AI-facing guide documents |
| `scripts/` | Automation scripts |

## 5. Do Not Confuse Template Files

These files are different:

```text
project-templates/AGENTS.md
templates/project-docs-template/AGENTS.md
```

| File | Role |
|---|---|
| `project-templates/AGENTS.md` | Used when maintaining the template repository |
| `templates/project-docs-template/AGENTS.md` | Copied into new docs projects |

The same distinction applies to `CLAUDE.md` and `_project/`.

## 6. General Codex Prompt Pattern

Use this prompt structure:

```text
작업 대상은 project-templates 루트입니다.

목표:
- [작업 목표]

범위:
- 수정 가능: [수정할 경로]
- 수정 금지: [수정하지 않을 경로]

제약:
- 루트 AGENTS.md와 templates/*/AGENTS.md의 역할을 혼동하지 마세요.
- 템플릿은 루트 1-depth 구조만 정의합니다.
- src 내부 구조는 템플릿에 강제하지 마세요.
- shared/_project/는 공통 원본입니다.
- templates/*/_project/는 새 프로젝트에 복사될 템플릿 결과입니다.

완료 조건:
- [검증 기준]
```

## 7. Common Workflows

### 7.1 Update Repository Guide Documents

Use when editing files under `guides/`.

Prompt example:

```text
작업 대상은 project-templates 루트입니다.

guides/project-template-types.md 를 수정하세요.

목표:
- docs/wiki/coding 템플릿의 선택 기준을 명확히 정리합니다.
- 각 템플릿의 루트 1-depth 구조만 설명합니다.

제약:
- templates/ 하위 파일은 수정하지 마세요.
- shared/ 하위 파일은 수정하지 마세요.
- D 드라이브 로컬 프로젝트 상태 관리 내용은 포함하지 마세요.
```

### 7.2 Update a Template Root Structure

Use when modifying one template.

Prompt example:

```text
작업 대상은 project-templates 루트입니다.

templates/project-docs-template 의 루트 구조를 검토하고 필요한 최소 파일만 유지하세요.

제약:
- _project/ 내부 상세 구조는 변경하지 마세요.
- docs/ 내부 상세 구조는 강제하지 마세요.
- src/, notebooks/, tests/ 는 docs-template에 추가하지 마세요.
- 변경 사항을 guides/project-template-types.md 에 반영하세요.
```

### 7.3 Update Shared `_project` Files

Use when editing common rules, commands, or docs.

Prompt example:

```text
작업 대상은 project-templates 루트입니다.

shared/_project/rules/markdown-style.md 를 업데이트하세요.

목표:
- 모든 템플릿에 공통 적용할 Markdown 작성 규칙을 정리합니다.

제약:
- templates/*/_project/ 는 직접 수정하지 마세요.
- 동기화 스크립트가 없다면 shared/_project/ 만 수정하세요.
- 템플릿별 전용 규칙은 작성하지 마세요.
```

### 7.4 Synchronize Shared Files into Templates

Use after shared file updates.

Prompt example:

```text
작업 대상은 project-templates 루트입니다.

shared/_project/ 의 공통 파일을 templates/project-*/_project/ 로 동기화하는 스크립트를 작성하거나 갱신하세요.

요구사항:
- 공통 파일은 각 템플릿으로 복사합니다.
- 템플릿별 추가 파일은 삭제하지 않습니다.
- 변경된 파일 목록을 출력합니다.
- dry-run 옵션을 지원합니다.
```

### 7.5 Validate Template Structures

Use when checking consistency.

Prompt example:

```text
작업 대상은 project-templates 루트입니다.

templates/ 하위 3개 템플릿의 루트 구조를 검증하는 스크립트를 작성하세요.

검증 대상:
- project-docs-template
- project-wiki-template
- project-coding-template

검증 기준:
- 필수 루트 파일과 폴더가 있는지 확인
- 불필요한 루트 폴더가 없는지 확인
- _project/ 내부 상세는 검증하지 않음
```

## 8. Recommended Codex Safety Rules

Codex should follow these safety rules.

| Rule | Description |
|---|---|
| Always state the working root | Avoid editing the wrong repository |
| Separate repository-level and template-level files | Avoid confusing root `AGENTS.md` with template `AGENTS.md` |
| Avoid broad destructive edits | Do not delete files unless explicitly requested |
| Keep templates shallow | Do not overdefine `src/`, `docs/contents/`, or `_project/` internals |
| Update guides after structural changes | Documentation must match template structure |
| Prefer shared source for common files | Edit `shared/_project/` instead of duplicated template copies |

## 9. Git Workflow for Template Repository

Recommended simple workflow:

```bash
git status
git checkout -b stage/update-template-guides
# edit files
git add .
git commit -m "Update template guide documents"
git checkout main
git merge stage/update-template-guides
git push origin main
```

For small changes, direct commits to `main` may be acceptable for personal projects.

For larger changes, use a stage branch.

## 10. Commit Message Examples

```text
Add project template type guide
Update shared project file policy
Refine docs template root structure
Add new project creation workflow
Add Codex template management workflow
```

## 11. Review Checklist Before Commit

Before committing Codex changes, check:

```text
[ ] Did Codex modify only the intended paths?
[ ] Are root-level and template-level AGENTS.md files still distinct?
[ ] Are template root structures still shallow?
[ ] Did guide documents reflect structural changes?
[ ] Were shared files edited in shared/_project/ when appropriate?
[ ] Were generated project examples kept out of the template repository?
```

## 12. Non-Goals

This workflow does not define how to manage the local D drive project status folders.

It does not manage:

```text
00_review/
20_active/
80_done/
90_archive/
99_deprecated/
```

Those are covered by the local D drive project management document.

## 13. Summary

When using Codex with `project-templates`:

- open the `project-templates` root in VS Code
- clearly state the work target
- distinguish root management files from template files
- edit `shared/_project/` for common files
- keep templates shallow and reusable
- update guides whenever structure changes
- validate before committing