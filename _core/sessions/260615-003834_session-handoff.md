---
tags: [templates, session]
created: 2026-06-15
updated: 2026-06-15
---

# project-templates 4차 세션 핸드오프

> 작성일시: 260615-003834
> 세션 목적: shared/ SSOT 파일 작성, wiki-template 구조 정의
> 이전 핸드오프: `_core/sessions/260614-235742_session-handoff.md`

## 1. 세션 핵심 요약

- `shared/` 에 공통 빈 폴더 추가 (`inbox/`, `sources/`, `docs/`, `outputs/`, `_core/sessions/`)
- `shared/_core/docs/` 에 공통 관리 파일 3종 추가: `project-log.md`, `project-spec.md`, `project-todo.md`
- 3개 템플릿에 동기화 완료
- `_core/docs/design-log.md` 신규 생성 (이 레포 템플릿 설계 이력)
- `CLAUDE.md`, `core-guide.md` 에 메타 레포 목적 및 하위 프로젝트 독립성 원칙 명시
- `sync-guide.md` 제외 대상에 `README.md`, `.gitignore`, `project-guide.md` 추가
- `project-wiki-template` 전용 구조 정의: `CLAUDE.md` 재작성, `wiki-rules.md` 신규 작성
- 전체 커밋 완료 (`8853290`)

## 2. 확정된 결정사항

| 항목 | 확정 내용 |
|---|---|
| 이 레포의 본질 | 하위 프로젝트를 설계하는 메타 레포. 하위 프로젝트 작업은 이 레포 범위 밖 |
| 하위 프로젝트 독립성 | 진행상황 관리·할일 관리·문서 작성이 완전히 독립적으로 수행됨 |
| shared/ SSOT 범위 | `_core/docs/`, `_core/rules/`, `_core/commands/`, `_core/sessions/`, 공통 빈 폴더 |
| sync 제외 파일 | `README.md`, `.gitignore`, `_core/docs/project-guide.md` — 각 템플릿에서 독립 정의 |
| design-log.md 역할 | 이 레포의 템플릿 설계 이력 기록. 하위 프로젝트 작업 이력 아님 |
| wiki-template 전용 파일 | `CLAUDE.md` (wiki 원칙 포함), `_core/rules/wiki-rules.md` (LLM Wiki Policy) |

## 3. 현재 파일 구조

```text
shared/
├── _core/
│   ├── rules/
│   │   ├── agent-rules.md
│   │   └── markdown-rules.md
│   ├── commands/
│   │   └── session-handoff.md
│   ├── docs/
│   │   ├── project-log.md    ← 신규
│   │   ├── project-spec.md   ← 신규
│   │   └── project-todo.md   ← 신규
│   └── sessions/
├── inbox/
├── sources/
├── docs/
└── outputs/
```

## 4. 미결 사항

| # | 항목 | 현재 상태 |
|---|---|---|
| 1 | `project-coding-template` 전용 구조 정의 | 미착수 |
| 2 | `project-docs-template` CLAUDE.md 참조 경로 갱신 | project-spec, project-todo 추가 필요 |
| 3 | `_core/refs/` 파일 삭제 | 사용자가 직접 수행 예정 |

## 5. 다음 작업 목록

| 우선순위 | 작업 | 비고 |
|---|---|---|
| 1 | `project-coding-template` 전용 구조 정의 | CLAUDE.md 재작성, coding-rules.md 작성 |
| 2 | `project-docs-template` CLAUDE.md 참조 경로 갱신 | project-spec.md, project-todo.md 추가 |
| 3 | 3개 템플릿 AGENTS.md 점검 | CLAUDE.md 와 정합성 확인 |

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.
이 내용을 기반으로 `project-coding-template` 전용 구조 정의 작업을 진행해 주세요.

워크스페이스 경로: `/mnt/d/projects/projects-templates`

우선적으로 다룰 항목:
1. `project-coding-template/CLAUDE.md` 재작성 — coding 전용 구조, 자료 흐름, 행동 규칙 반영
2. `project-coding-template/_core/rules/coding-rules.md` 작성 — 코딩 컨벤션, 폴더 규칙, 실험 관리 등
3. `project-docs-template/CLAUDE.md` 참조 경로 갱신 — `project-spec.md`, `project-todo.md` 추가

참고 파일:
- 핸드오프: `_core/sessions/260615-003834_session-handoff.md`
- wiki-template 참고: `templates/project-wiki-template/CLAUDE.md`, `_core/rules/wiki-rules.md`
- 레거시 참고: `/mnt/d/projects/nampluskr/99_deprecated/20260607_project_templates/CLAUDE.md`

## 7. 참고 자료

| 항목 | 경로 |
|---|---|
| 동기화 스크립트 | `_core/scripts/sync_shared.py` |
| 동기화 가이드 | `_core/docs/sync-guide.md` |
| 설계 이력 | `_core/docs/design-log.md` |
| wiki 운영 규칙 | `templates/project-wiki-template/_core/rules/wiki-rules.md` |
