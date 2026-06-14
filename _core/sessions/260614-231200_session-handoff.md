---
tags: [templates, session]
created: 2026-06-14
updated: 2026-06-14
---

# project-templates 초기 구축 세션 핸드오프

> 작성일시: 260614-231200
> 세션 목적: project-templates 레포 워크스페이스 초기 구조 설계 및 구현
> 이전 핸드오프: 없음

## 1. 세션 핵심 요약

- `_refs/` 의 4개 참조 문서를 검토하여 전체 설계 방향을 파악
- `nampluskr/_core/` 운영 체계를 이 레포에 적용하기로 결정 (`_project/` → `_core/` 대체)
- `_core/`, `shared/`, `templates/` (3개 템플릿) 골격 생성
- 루트 `CLAUDE.md`, `AGENTS.md` 생성 및 sync_agents.py 동기화 검증
- `_core/rules/` 3개 파일 작성 후 markdown-rules.md 원본 적용
- 검토 후 README.md, CLAUDE.md, AGENTS.md, agent-rules.md, template-rules.md 수정

## 2. 사용자 요청 및 의도

각 요청과 그 배경 목적은 다음과 같다.

| 요청 내용 | 배경 목적 |
|---|---|
| `_refs/` 문서 내용 검토 | 구현 전 설계 방향 정렬 |
| `_core/` 및 `templates/` 생성 | 워크스페이스 골격 구축 |
| 루트 `CLAUDE.md`, `AGENTS.md` 생성 | sync_agents.py 동기화 체계 적용 |
| `nampluskr/_core/markdown-rules.md` 원본 적용 | 전 워크스페이스 문서 작성 규칙 통일 |
| 3단계(README / CLAUDE+AGENTS / `_core/rules/`) 검토 후 수정 | 내용 품질 및 일관성 확보 |

## 3. 확정된 결정사항

이 세션에서 최종 결정된 사항은 다음과 같다.

| 항목 | 확정 내용 | 비고 |
|---|---|---|
| 운영 폴더명 | `_project/` 대신 `_core/` 사용 | `nampluskr` 체계와 통일 |
| `_core/` 위치 | 레포 루트 + 각 템플릿 내부 + `shared/` | 역할 구분 필수 |
| 공통 파일 SSOT | `shared/_core/` | 템플릿별 `_core/` 직접 수정 금지 |
| 마크다운 규칙 | `nampluskr/_core/rules/markdown-rules.md` 원본 그대로 | tags만 `templates`로 변경 |
| sync 대상 섹션 | `## 2.`~`## 5.` (CLAUDE.md → AGENTS.md) | 검증 완료 |
| `_refs/` 처리 | 참조 전용 유지, 수정 금지 | guides/ 이동 미결 |

## 4. 미결 사항

다음 세션에서 결정 또는 구현이 필요한 항목은 다음과 같다.

| # | 항목 | 현재 상태 | 결정 필요 내용 |
|---|---|---|---|
| 1 | `guides/` 생성 | 폴더 없음 | `_refs/` 문서를 guides/로 이동할지, 별도 작성할지 |
| 2 | `scripts/` 생성 | 폴더 없음 | `sync_shared.py`, `create_project.py` 구현 범위 |
| 3 | `.gitignore` 생성 | 루트에 없음 | 레포 루트 .gitignore 작성 필요 |
| 4 | `shared/_core/` ↔ `templates/*/_core/` 동기화 검증 | 수동 복사 상태 | sync_shared.py 구현 후 실제 동기화로 전환 |
| 5 | 각 템플릿 `AGENTS.md` template 표기 수정 | `project-wiki-template` AGENTS.md에 template 표기 미확인 | 전체 점검 필요 |

## 5. 다음 작업 목록

다음 세션에서 수행할 작업을 우선순위 순으로 정리한다.

| 우선순위 | 작업 | 관련 파일 |
|---|---|---|
| 1 | 루트 `.gitignore` 생성 | `.gitignore` |
| 2 | `guides/` 생성 및 문서 작성 | `guides/` |
| 3 | `scripts/sync_shared.py` 구현 | `scripts/sync_shared.py` |
| 4 | `scripts/create_project.py` 구현 | `scripts/create_project.py` |
| 5 | 각 템플릿 파일 전체 점검 (AGENTS.md template 표기 등) | `templates/*/` |

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.
이 내용을 기반으로 미결 사항 처리 및 다음 작업을 진행해 주세요.

워크스페이스 경로: `/mnt/d/projects/projects-templates`
운영 체계 참조: `nampluskr/_core/` 구조를 이 레포에 동일하게 적용 중

특히 다음 항목을 우선적으로 다뤄주세요:
1. 루트 `.gitignore` 생성
2. `guides/` 폴더 및 문서 생성
3. `scripts/sync_shared.py` 구현

참고 파일:
- 핸드오프: `_core/sessions/260614-231200_session-handoff.md`
- 운영 규칙: `_core/rules/agent-rules.md`, `_core/rules/template-rules.md`
- 커맨드: `_core/commands/new-project.md`, `_core/commands/sync-shared.md`

## 7. 참고 자료

이 세션과 관련된 파일은 다음과 같다.

| 항목 | 경로 | 용도 |
|---|---|---|
| 참조 문서 원본 | `_refs/` | 초기 설계 아이디어 출처 |
| 워크스페이스 운영 원본 | `/mnt/d/projects/nampluskr/_core/` | 운영 체계 참조 모델 |
| sync_agents.py | `/mnt/d/projects/nampluskr/_core/scripts/sync_agents.py` | CLAUDE.md↔AGENTS.md 동기화 스크립트 |
