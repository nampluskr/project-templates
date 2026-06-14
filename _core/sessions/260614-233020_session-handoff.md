---
tags: [templates, session]
created: 2026-06-14
updated: 2026-06-14
---

# project-templates 2차 세션 핸드오프

> 작성일시: 260614-233020
> 세션 목적: 미결 사항 처리 — .gitignore, 템플릿 점검, _core/docs, _core/scripts 구축
> 이전 핸드오프: `_core/sessions/260614-231200_session-handoff.md`

## 1. 세션 핵심 요약

- 루트 `.gitignore` 생성
- 3개 템플릿 `AGENTS.md` 템플릿 표기 오류 수정 (`project-docs-template` 고정 → 각자 맞는 값으로)
- `_refs/` → `_core/refs/` 이동 및 관련 경로 참조 일괄 수정
- `_core/docs/` 에 3개 문서 신규 작성 (`template-guide`, `sync-guide`, `new-project-guide`)
- `_core/docs/core-guide.md` 수정 (구조 트리, 폴더 테이블 갱신)
- `_core/scripts/sync_shared.py` 구현 및 동작 검증
- `_core/scripts/create_project.py` 구현 및 동작 검증
- 커밋 메세지 제안 후 세션 종료

## 2. 사용자 요청 및 의도

| 요청 내용 | 배경 목적 |
|---|---|
| 이전 핸드오프 이어서 작업 — 1번, 2번만 진행 | `.gitignore` 생성 + 템플릿 AGENTS.md 표기 점검 |
| `_refs/` → `_core/refs/` 이동 | 참조 문서를 `_core/` 체계 안으로 통합 |
| `_core/docs/` 문서 목록 제안 → 3개 작성 + core-guide 수정 | 가이드 문서 체계 구축 (`guides/` 대체) |
| `_core/scripts/` 에 스크립트 생성 | 동기화 및 프로젝트 생성 자동화 |
| 커밋 후 세션 핸드오프 | 작업 상태 보존 |

## 3. 확정된 결정사항

| 항목 | 확정 내용 | 비고 |
|---|---|---|
| `guides/` 폴더 | 생성하지 않음 — `_core/docs/` 로 대체 | CLAUDE.md 구조 트리도 이미 반영됨 |
| 참조 문서 위치 | `_core/refs/` | `_refs/` 에서 이동 |
| 스크립트 위치 | `_core/scripts/` | 루트 `scripts/` 대신 사용 |
| `sync_shared.py` 호출 경로 | `python _core/scripts/sync_shared.py` | 커맨드 파일에 반영 완료 |
| `create_project.py` 호출 경로 | `python _core/scripts/create_project.py` | 커맨드 파일에 반영 완료 |

## 4. 미결 사항

| # | 항목 | 현재 상태 | 결정 필요 내용 |
|---|---|---|---|
| 1 | `shared/_core/` 누락 파일 | `rules/` 2개 + `commands/` 1개만 존재 | `template-rules.md`, `new-project.md`, `sync-shared.md` 추가 여부 |
| 2 | `templates/*/_core/` ↔ `shared/_core/` 동기화 실행 | dry-run 확인 완료 (9개 파일 변경 예정) | `--apply` 실행 승인 필요 |
| 3 | CLAUDE.md 구조 트리 `scripts/` 항목 | `_core/scripts/` 로 이동했으나 CLAUDE.md 트리에 미반영 | 수정 필요 |
| 4 | 커밋 | 메세지 제안까지 완료, 실제 커밋 미실행 | 사용자 승인 후 실행 |

## 5. 다음 작업 목록

| 우선순위 | 작업 | 관련 파일 |
|---|---|---|
| 1 | 커밋 실행 | — |
| 2 | CLAUDE.md 구조 트리 `scripts/` 항목 수정 | `CLAUDE.md` |
| 3 | `sync_shared.py --apply` 실행하여 `templates/*/_core/` 동기화 | `_core/scripts/sync_shared.py` |
| 4 | `shared/_core/` 누락 파일 추가 여부 결정 및 처리 | `shared/_core/` |

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.
이 내용을 기반으로 미결 사항 처리 및 다음 작업을 진행해 주세요.

워크스페이스 경로: `/mnt/d/projects/projects-templates`

특히 다음 항목을 우선적으로 다뤄주세요:
1. 커밋 실행 (메세지 제안까지 완료된 상태)
2. CLAUDE.md 구조 트리 `scripts/` 항목 수정
3. `sync_shared.py --apply` 로 `templates/*/_core/` 동기화

참고 파일:
- 핸드오프: `_core/sessions/260614-233020_session-handoff.md`
- 이전 핸드오프: `_core/sessions/260614-231200_session-handoff.md`
- 운영 규칙: `_core/rules/agent-rules.md`, `_core/rules/template-rules.md`
- 스크립트: `_core/scripts/sync_shared.py`, `_core/scripts/create_project.py`

## 7. 참고 자료

| 항목 | 경로 | 용도 |
|---|---|---|
| 동기화 스크립트 | `_core/scripts/sync_shared.py` | `shared/_core/` → `templates/*/_core/` 동기화 |
| 프로젝트 생성 스크립트 | `_core/scripts/create_project.py` | 템플릿 복사 및 플레이스홀더 안내 |
| 동기화 가이드 | `_core/docs/sync-guide.md` | 동기화 구조 및 원칙 |
| 공통 파일 원본 | `shared/_core/` | 동기화 SSOT |
