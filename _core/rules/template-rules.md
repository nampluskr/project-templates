---
tags: [templates, rules]
created: 2026-06-14
updated: 2026-06-14
---

# template-rules.md

이 워크스페이스에서 템플릿을 설계하고 유지하는 규칙을 정의한다.

## 1. 템플릿 구조 원칙

각 템플릿은 다음 원칙을 따른다.

- 루트 1-depth 구조만 정의한다. 내부 상세 구조는 강제하지 않는다.
- 필수 파일: `README.md`, `AGENTS.md`, `CLAUDE.md`, `.gitignore`, `_core/`
- `_core/` 내용은 `shared/_core/` 에서 동기화한다. 템플릿별로 직접 수정하지 않는다.
- 템플릿 간 공통 파일은 `shared/` 에서 관리하고 각 템플릿으로 배포한다.

## 2. 템플릿 종류 및 전용 폴더

이 워크스페이스에서 관리하는 템플릿과 각 템플릿의 전용 폴더는 다음과 같다.

| 템플릿 | 공통 폴더 | 전용 폴더 |
|---|---|---|
| `project-docs-template` | `_core/`, `docs/`, `outputs/` | `inbox/`, `sources/` |
| `project-wiki-template` | `_core/`, `docs/`, `outputs/` | `inbox/`, `sources/`, `wiki/` |
| `project-coding-template` | `_core/`, `docs/`, `outputs/` | `data/`, `src/`, `scripts/`, `notebooks/`, `tests/`, `configs/`, `experiments/` |

## 3. shared/ 동기화 원칙

공통 파일은 `shared/_core/` 를 SSOT로 관리한다.

- `shared/_core/` 를 수정한 후 `scripts/sync_shared.py` 로 각 템플릿에 배포한다.
- 배포는 덮어쓰기 방식이다. 템플릿별 `_core/` 에 추가된 전용 파일은 삭제하지 않는다.
- 배포 전 반드시 dry-run으로 변경 대상을 확인한다.

## 4. 새 프로젝트 생성 원칙

새 프로젝트 생성 시 지켜야 할 원칙은 다음과 같다.

- 새 프로젝트는 반드시 이 레포와 독립된 Git 레포로 만든다.
- 생성 후 프로젝트 내부 파일은 이 레포 범위 밖이다.
- 생성 절차는 `_core/commands/new-project.md` 를 따른다.

## 5. 금지 사항

다음 사항은 템플릿에 추가하지 않는다.

- `src/` 내부 패키지 구조를 강제하는 파일
- 실제 프로젝트 코드나 데이터
- `project-docs-template` 에 `src/`, `notebooks/`, `tests/`
- `project-wiki-template` 에 `src/`, `tests/`
