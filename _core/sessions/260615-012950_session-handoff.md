---
tags: [templates, session]
created: 2026-06-15
updated: 2026-06-15
---

# project-templates 6차 세션 핸드오프

> 작성일시: 260615-012950
> 세션 목적: 3개 템플릿 AGENTS.md 정합성 점검, 커스텀 명령어 6종 추가
> 이전 핸드오프: `_core/sessions/260615-011941_session-handoff.md`

## 1. 세션 핵심 요약

- 3개 템플릿 `AGENTS.md` 점검 완료 — §2 구조, §3 핵심 행동 규칙 CLAUDE.md 수준으로 수정
- 커스텀 명령어 6종 신규 작성 — `shared/_core/commands/` SSOT → 3개 템플릿 동기화
- 3개 템플릿 `CLAUDE.md` 참조 경로 표에 신규 커맨드 7개 항목 추가
- 3개 템플릿 `project-guide.md` `_core/` 구조도 갱신 — 구버전(session-handoff.md만) → 전체 파일 반영

## 2. 사용자 요청 및 의도

| 요청 내용 | 배경 목적 |
|---|---|
| 3개 템플릿 AGENTS.md 점검 | 5차 세션 미결 사항 처리 — CLAUDE.md 변경 후 정합성 확인 |
| deprecated 커맨드 6종 현행화 | 하위 프로젝트에서 세션·프로젝트 관리 커맨드를 사용할 수 있도록 |

## 3. 확정된 결정사항

| 항목 | 확정 내용 | 비고 |
|---|---|---|
| AGENTS.md §3 규칙 | CLAUDE.md §4/§5와 동일 수준으로 맞춤 | docs-rules, python-rules, wiki-rules, coding-rules 참조 명시 |
| wiki AGENTS.md §2 | `wiki/` 폴더 추가 | 구버전에 누락되어 있었음 |
| coding AGENTS.md §2 | CLAUDE.md 구조와 동일하게 전면 교체 | data/src/scripts/notebooks/tests/configs/experiments 추가 |
| 커맨드 SSOT | `shared/_core/commands/` | `project-guide.md`는 shared SSOT 아님 — 템플릿별 직접 관리 |
| 커맨드 파일 참조 경로 | `_project/` → `_core/docs/`, `_core/sessions/` | deprecated 경로 현행화 |
| PROJECT-HISTORY.md | → `project-log.md` | 현행 파일명으로 통일 |
| AGENTS.md 커맨드 목록 | 추가 안 함 | Codex는 agent-rules.md 경유로 커맨드 인지 |

## 4. 미결 사항

없음.

## 5. 다음 작업 목록

| 우선순위 | 작업 | 관련 파일 | 비고 |
|---|---|---|---|
| 1 | `_core/refs/` 파일 삭제 | `_core/refs/` | 사용자가 직접 수행 예정 |
| 2 | `create_project.py` 커맨드 파일 복사 로직 추가 | `_core/scripts/create_project.py` | 신규 커맨드 6종이 새 프로젝트 생성 시 포함되는지 확인 |

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.

워크스페이스 경로: `/mnt/d/projects/projects-templates`

우선적으로 다룰 항목:
1. `_core/scripts/create_project.py` 를 열어 커맨드 파일 복사 로직 확인
2. 신규 커맨드 6종(`session-start`, `session-end`, `project-init`, `project-status`, `project-update`, `commit-message`)이 새 프로젝트 생성 시 자동 포함되는지 점검
3. 누락 시 복사 로직 추가

참고 파일:
- 핸드오프: `_core/sessions/260615-012950_session-handoff.md`
- 생성 스크립트: `_core/scripts/create_project.py`

## 7. 참고 자료

| 항목 | 경로 | 용도 |
|---|---|---|
| 동기화 스크립트 | `_core/scripts/sync_shared.py` | shared → templates 동기화 |
| 생성 스크립트 | `_core/scripts/create_project.py` | 새 프로젝트 생성 |
| 커맨드 SSOT | `shared/_core/commands/` | 커스텀 명령어 원본 |
