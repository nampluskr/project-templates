---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# sync-guide.md

`shared/_core/` 와 `templates/*/_core/` 간 동기화 방법과 주의사항을 설명한다.

## 1. 동기화 구조

이 레포에는 `_core/` 가 두 맥락에서 존재한다.

| 경로 | 역할 |
|---|---|
| `project-templates/_core/` | 이 레포 자체 운영 파일. 새 프로젝트에 복사되지 않음 |
| `shared/_core/` | 각 템플릿의 `_core/` 원본 (SSOT) |
| `templates/*/_core/` | `shared/_core/` 에서 동기화된 결과. 새 프로젝트 생성 시 복사됨 |

## 2. 동기화 원칙

공통 파일 관리 원칙은 다음과 같다.

- `shared/_core/` 를 수정한 후 `scripts/sync_shared.py` 로 각 템플릿에 배포한다.
- 배포는 덮어쓰기 방식이다. 템플릿별 `_core/` 에 추가된 전용 파일은 삭제하지 않는다.
- 배포 전 반드시 dry-run으로 변경 대상을 확인한다.
- 템플릿별 `_core/` 를 직접 수정하지 않는다.

## 3. 동기화 대상 파일

`shared/_core/` 에서 관리하는 공통 파일 목록은 다음과 같다.

| 파일 | 경로 |
|---|---|
| 에이전트 행동 규칙 | `shared/_core/rules/agent-rules.md` |
| 마크다운 작성 규칙 | `shared/_core/rules/markdown-rules.md` |
| 세션 핸드오프 커맨드 | `shared/_core/commands/session-handoff.md` |

## 4. 동기화 절차

공통 파일 수정 후 동기화 절차는 다음과 같다.

1. `shared/_core/` 에서 파일 수정
2. `sync-shared` 커맨드 실행 (dry-run)
3. 변경 대상 확인
4. `sync-shared` 커맨드 실행 (`--apply`)
5. `templates/*/_core/` 결과 검증

상세 절차는 `_core/commands/sync-shared.md` 를 참조한다.

## 5. 템플릿별 전용 파일

각 템플릿의 `_core/` 에는 공통 파일 외에 템플릿 전용 파일이 추가될 수 있다.

전용 파일은 `shared/_core/` 에 포함하지 않으며 동기화 시 삭제되지 않는다.

| 템플릿 | 전용 파일 예시 |
|---|---|
| `project-docs-template` | (현재 없음) |
| `project-wiki-template` | (현재 없음) |
| `project-coding-template` | (현재 없음) |
