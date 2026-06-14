---
tags: [templates, session]
created: 2026-06-15
updated: 2026-06-15
---

# project-templates 5차 세션 핸드오프

> 작성일시: 260615-011941
> 세션 목적: project-coding-template 전용 구조 정의, 공통 규칙 파일 정비
> 이전 핸드오프: `_core/sessions/260615-003834_session-handoff.md`

## 1. 세션 핵심 요약

- `project-coding-template/CLAUDE.md` 재작성 — 자료 흐름 섹션 추가, 참조 경로 완성
- `project-coding-template/_core/rules/coding-rules.md` 신규 작성 — LLM 코딩 행동 규칙 10개 항목
- `project-coding-template/_core/docs/coding-guide.md` 신규 작성 — 사람용 코딩 운영 가이드
- `project-docs-template/CLAUDE.md` 참조 경로 갱신 — `project-spec.md`, `project-todo.md` 추가
- `markdown-rules.md` → `docs-rules.md` 전체 이름 변경 (shared + 3개 템플릿 + 메타 레포)
- 3개 템플릿 CLAUDE.md 핵심 행동 규칙에 docs-rules / python-rules 적용 조건 명시
- `shared/_core/docs/subject-guide.md` 신규 작성 → 3개 템플릿 동기화
- `shared/_core/rules/python-rules.md` 신규 작성 → 3개 템플릿 동기화
- `shared/_core/rules/agent-rules.md` §4 "규칙 적용 기준" 섹션 추가 → 3개 템플릿 동기화
- `_core/scripts/sync_shared.py`, `create_project.py` — python-rules.md 적용 (pathlib→os.path, 파일 헤더 주석)
- `coding-rules.md` §5 파일 헤더 주석 형식 수정 — 한국어→영어, `# filename.py: 설명` 형식

## 2. 사용자 요청 및 의도

| 요청 내용 | 배경 목적 |
|---|---|
| coding-template CLAUDE.md 재작성 | wiki-template 수준으로 완성도 맞추기 |
| coding-rules.md 작성 | LLM 코딩 실수 방지 행동 지침 정의 |
| markdown-rules → docs-rules 이름 변경 | 문서 규칙임을 명확히 표현 |
| 3개 템플릿에 규칙 적용 원칙 명시 | 작업 유형별 적용 규칙을 에이전트가 혼동하지 않도록 |
| subject-guide.md 작성 및 shared 동기화 | 하위 프로젝트에서 태그·파일명·frontmatter 분류 기준 통일 |
| python-rules.md 작성 및 적용 | Python 코드 작성 시 스타일 일관성 확보 |
| 파일 헤더 주석 형식 확정 | `# filename.py: English description` 형식으로 통일 |

## 3. 확정된 결정사항

| 항목 | 확정 내용 | 비고 |
|---|---|---|
| docs-rules.md | 문서 작성 규칙 파일명 (구 markdown-rules.md) | 전체 치환 완료 |
| python-rules.md | Python 코드 작성 규칙. shared SSOT | 3개 템플릿 동기화 완료 |
| coding-rules.md | coding-template 전용 에이전트 행동 규칙 | shared 대상 아님 |
| 파일 헤더 주석 | `# filename.py: English one-line description.` | coding-rules §5, python-rules §3.1 일치 |
| 경로 표기 | `os.path` 사용. `pathlib.Path` 금지 | python-rules §2.1 |
| 규칙 적용 기준 | 마크다운→docs-rules, Python→python-rules | agent-rules §4, 각 CLAUDE.md 명시 |
| subject-guide.md 위치 | `shared/_core/docs/` SSOT, 메타 레포 _core/docs 에는 없음 | 3개 템플릿 동기화 완료 |

## 4. 미결 사항

| # | 항목 | 현재 상태 | 결정 필요 내용 |
|---|---|---|---|
| 1 | 3개 템플릿 AGENTS.md 정합성 점검 | 미착수 | CLAUDE.md 변경 후 AGENTS.md 참조 경로 일치 확인 |
| 2 | `_core/refs/` 파일 삭제 | 사용자가 직접 수행 예정 | — |

## 5. 다음 작업 목록

| 우선순위 | 작업 | 관련 파일 | 비고 |
|---|---|---|---|
| 1 | 3개 템플릿 AGENTS.md 점검 | `templates/*/AGENTS.md` | CLAUDE.md 참조 경로와 정합성 확인 |
| 2 | `_core/refs/` 파일 삭제 | `_core/refs/` | 사용자가 직접 수행 예정 |

## 6. 다음 세션 시작 지시문

아래는 이전 세션의 컨텍스트입니다.
이 내용을 기반으로 3개 템플릿 AGENTS.md 점검 작업을 진행해 주세요.

워크스페이스 경로: `/mnt/d/projects/projects-templates`

우선적으로 다룰 항목:
1. `templates/*/AGENTS.md` 를 열어 각 CLAUDE.md 참조 경로와 불일치 항목 확인
2. docs-rules.md, python-rules.md, coding-rules.md, subject-guide.md 참조 누락 여부 점검
3. 필요한 경우 수정

참고 파일:
- 핸드오프: `_core/sessions/260615-011941_session-handoff.md`
- 규칙 적용 기준: `shared/_core/rules/agent-rules.md` §4

## 7. 참고 자료

| 항목 | 경로 | 용도 |
|---|---|---|
| 동기화 스크립트 | `_core/scripts/sync_shared.py` | shared → templates 동기화 |
| 공통 에이전트 규칙 | `shared/_core/rules/agent-rules.md` | 규칙 적용 기준 포함 |
| Python 규칙 | `shared/_core/rules/python-rules.md` | Python 코드 스타일 |
| 코딩 행동 규칙 | `templates/project-coding-template/_core/rules/coding-rules.md` | coding-template 전용 |
| 주제 분류 | `shared/_core/docs/subject-guide.md` | 태그·파일명·frontmatter 분류 기준 |
