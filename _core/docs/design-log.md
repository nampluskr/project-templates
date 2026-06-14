---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-15
---

# design-log.md

이 레포의 템플릿 설계 이력을 기록한다.
에이전트가 구조 변경, 설계 결정, 정책 확정 후 갱신한다.

| Date | 내용 | 비고 |
|---|---|---|
| 2026-06-14 | 레포 초기 구성 — `_core/`, `shared/`, `templates/` 3개 템플릿 구조 정의 | |
| 2026-06-14 | `_core/refs/` 내용을 `_core/docs/` 에 반영 | refs 삭제 예정 |
| 2026-06-14 | `sync_shared.py` 동기화 범위 `shared/_core/` → `shared/` 전체로 확장 | |
| 2026-06-14 | `project-coding-template` 에 `inbox/`, `sources/` 추가 | template-guide.md 정합성 확보 |
| 2026-06-15 | `shared/` 에 공통 빈 폴더 추가 — `inbox/`, `sources/`, `docs/`, `outputs/`, `_core/sessions/` | |
| 2026-06-15 | `README.md`, `.gitignore` sync 제외 결정 — 템플릿별 독립 관리 | |
| 2026-06-15 | 워크스페이스 목적 명시 — 하위 프로젝트 설계 메타 레포, 하위 프로젝트 작업은 이 레포 범위 밖 | CLAUDE.md, core-guide.md 반영 |
