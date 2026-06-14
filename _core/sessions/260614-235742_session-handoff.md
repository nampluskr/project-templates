---
tags: [templates, session]
created: 2026-06-14
updated: 2026-06-14
---

# project-templates 3차 세션 핸드오프

> 작성일시: 260614-235742
> 세션 목적: refs 문서 내용을 docs에 반영, 동기화 범위 확장, 템플릿 구조 정합성 점검
> 이전 핸드오프: `_core/sessions/260614-233020_session-handoff.md`

## 1. 세션 핵심 요약

- `_core/refs/` 문서 5개 내용을 현재 구조에 맞게 `_core/docs/` 에 반영 완료
- `sync_shared.py` 동기화 범위를 `shared/_core/` → `shared/` 전체로 확장
- `_core/commands/sync-shared.md` 설명 갱신 (새 동기화 범위 반영)
- `project-coding-template` 에 `inbox/`, `sources/` 폴더 추가 (template-guide.md 와 정합성 확보)
- 전체 작업 커밋 완료 (`4df3248`)

## 2. 사용자 요청 및 의도

| 요청 내용 | 배경 목적 |
|---|---|
| refs 문서 내용을 관련 docs에 상세히 반영 | refs 파일 삭제 전 내용 보존 및 현재 구조에 통합 |
| sync_shared.py 가 shared/ 전체를 동기화하는지 확인 | shared/ 에 _core 외 파일 추가 시 자동 반영되도록 |
| 템플릿 구조와 template-guide.md 일치 여부 확인 | 문서와 실제 구조의 정합성 확보 |
| 세션 핸드오프 실행 | 다음 세션 — shared/ 에 project-docs-template 공통 파일 작성 |

## 3. 확정된 결정사항

| 항목 | 확정 내용 | 비고 |
|---|---|---|
| sync 범위 | `shared/` 전체 → `templates/*/` | 기존: `shared/_core/` → `templates/*/_core/` |
| refs 처리 방침 | 참조 전용 (삭제 예정) — docs에 내용 반영 완료 | 삭제는 사용자가 직접 진행 |
| coding template 구조 | `inbox/`, `sources/` 추가 | template-guide.md 정의와 일치 |
| docs 반영 완료 파일 | `core-guide.md`, `sync-guide.md`, `new-project-guide.md`, `template-guide.md` | refs 5개 파일 내용 모두 반영 |

## 4. 미결 사항

| # | 항목 | 현재 상태 | 결정 필요 내용 |
|---|---|---|---|
| 1 | `shared/` 공통 파일 작성 | `shared/_core/` 만 존재 | `project-docs-template` 기준으로 공통 파일 작성 필요 |
| 2 | `_core/refs/` 파일 삭제 | 내용 반영 완료, 파일은 존재 중 | 사용자 확인 후 삭제 |

## 5. 다음 작업 목록

| 우선순위 | 작업 | 관련 파일 | 비고 |
|---|---|---|---|
| 1 | `shared/` 에 `project-docs-template` 공통 파일 작성 | `shared/` | 아래 상세 참조 |
| 2 | `sync_shared.py --dry-run` 으로 새 공통 파일 동기화 대상 확인 | `_core/scripts/sync_shared.py` | |
| 3 | `sync_shared.py --apply` 로 3개 템플릿에 동기화 | `templates/*/` | |
| 4 | `_core/refs/` 파일 삭제 | `_core/refs/` | 사용자 승인 후 |

### 우선순위 1 상세: shared/ 공통 파일 작성

`shared-project-files-policy.md` 기준으로 아래 파일/폴더를 `shared/` 에 작성한다.

현재 `shared/` 구조:
```text
shared/
└── _core/
    ├── rules/
    │   ├── agent-rules.md
    │   └── markdown-rules.md
    └── commands/
        └── session-handoff.md
```

추가해야 할 파일/폴더 (`project-docs-template` 기준 공통 파일):
```text
shared/
├── README.md          ← 신규 (플레이스홀더 포함)
├── .gitignore         ← 신규
└── _core/             ← 기존 유지
```

`inbox/`, `sources/`, `docs/`, `outputs/` 는 빈 폴더이므로 `.gitkeep` 으로 관리하되,
이미 각 템플릿에 존재하므로 shared/ 에서 관리할지 여부를 확인한다.

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.
이 내용을 기반으로 `shared/` 폴더에 `project-docs-template` 기준 공통 파일을 작성하는 작업을 진행해 주세요.

워크스페이스 경로: `/mnt/d/projects/projects-templates`

우선적으로 다룰 항목:
1. `shared/` 에 추가할 공통 파일 목록 확정 (README.md, .gitignore, 빈 폴더 등)
2. 각 파일 작성 또는 기존 템플릿에서 복사 후 공통화
3. `sync_shared.py --dry-run` 으로 동기화 대상 확인
4. `sync_shared.py --apply` 로 3개 템플릿에 반영

참고 파일:
- 핸드오프: `_core/sessions/260614-235742_session-handoff.md`
- 동기화 정책: `_core/docs/sync-guide.md`
- 공통 파일 정책: `_core/refs/shared-project-files-policy.md` (삭제 예정, 내용은 sync-guide.md에 반영됨)
- 동기화 커맨드: `_core/commands/sync-shared.md`
- 동기화 스크립트: `_core/scripts/sync_shared.py`

## 7. 참고 자료

| 항목 | 경로 | 용도 |
|---|---|---|
| 동기화 스크립트 | `_core/scripts/sync_shared.py` | `shared/` → `templates/*/` 동기화 |
| 동기화 가이드 | `_core/docs/sync-guide.md` | 동기화 구조 및 원칙 |
| 템플릿 가이드 | `_core/docs/template-guide.md` | 3개 템플릿 구조 정의 |
| 공통 파일 원본 | `shared/` | 동기화 SSOT |
