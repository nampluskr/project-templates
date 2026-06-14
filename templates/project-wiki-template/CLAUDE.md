---
tags: [project, agent-config]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# CLAUDE.md — {{PROJECT_NAME}}

이 파일은 Claude Code가 이 프로젝트를 다룰 때 따르는 진입점 지침이다.
상세 규칙은 `_core/` 를 참조한다.

본 워크스페이스는 하나의 Git Repository 를 하나의 문서 프로젝트로 간주한다.
AI CLI 는 `wiki/` 에 지식을 지속적으로 누적·갱신하고, `wiki/` 를 기반으로 `docs/` 의 최종 문서를 작성·수정한다.

## 1. 프로젝트 개요

- **이름**: {{PROJECT_NAME}}
- **목적**: {{PROJECT_DESCRIPTION}}
- **템플릿**: `project-wiki-template`

## 2. 프로젝트 구조

```text
{{PROJECT_SLUG}}/
├── _core/        # 프로젝트 운영 파일
├── inbox/        # 미분류 입력 자료
├── sources/      # 정리된 참고 자료
├── wiki/         # 프로젝트 전용 지식 저장소 (SSOT)
├── docs/         # 최종 문서
└── outputs/      # 생성물, 빌드 결과
```

## 3. 폴더 역할

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 아직 분류하지 않은 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 (출처 보존) |
| `wiki/` | 프로젝트 전용 LLM Wiki 지식 저장소 — AI CLI 주요 작업 대상 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 빌드 결과, 내보내기 |

## 4. 자료 흐름

자료는 다음 순서로 이동한다.

```text
inbox/ → sources/ → wiki/ → docs/ → outputs/
```

| 단계 | 폴더 | 의미 |
|---|---|---|
| Capture | `inbox/` | 미분류 자료 임시 보관 |
| Source Management | `sources/` | 출처 확인된 원본 자료 정리 |
| Knowledge Distillation | `wiki/` | 개념·방법·예시 단위로 정제 |
| Publication | `docs/` | 최종 문서로 재구성 |

## 5. 핵심 행동 규칙

- 작업 전 `_core/rules/agent-rules.md` 를 참조한다.
- 마크다운 문서 작성·수정 시 `_core/rules/docs-rules.md` 를 따른다.
- Python 스크립트 작성·수정 시 `_core/rules/python-rules.md` 를 따른다.
- `wiki/` 운영은 `_core/rules/wiki-rules.md` 를 따른다.
- 새로운 정보는 우선 `wiki/` 에 반영한다. `docs/` 를 직접 수정하지 않는다.
- `wiki/` 문서 생성·수정 시 YAML frontmatter, 내부 링크, Related 섹션, index 문서를 함께 관리한다.
- `docs/` 수정 시 관련 `wiki/` 와의 정합성을 확인한다.
- 루트 폴더 구조는 변경하지 않는다.

## 6. wiki/ 운영 원칙

`wiki/` 는 이 프로젝트 전용 지식 저장소이자 `docs/` 의 SSOT 이다.

- 새로운 정보는 우선 `wiki/` 에 반영한다.
- `wiki/` 와 `docs/` 내용이 충돌하면 `wiki/` 를 먼저 검토하고 정정한다.
- `wiki/` 는 이 프로젝트의 주제 범위 안에서만 유지한다.
- 세부 운영 규칙, 문서 유형, frontmatter 표준, 링크 규칙, 문서 템플릿은 `_core/rules/wiki-rules.md` 를 참조한다.

## 7. 참조 경로

| 항목 | 경로 |
|---|---|
| 에이전트 규칙 | `_core/rules/agent-rules.md` |
| 마크다운 규칙 | `_core/rules/docs-rules.md` |
| Python 규칙 | `_core/rules/python-rules.md` |
| Wiki 운영 규칙 | `_core/rules/wiki-rules.md` |
| Wiki 운영 가이드 | `_core/docs/wiki-guide.md` |
| 주제 분류 | `_core/docs/subject-guide.md` |
| 프로젝트 가이드 | `_core/docs/project-guide.md` |
| 프로젝트 명세 | `_core/docs/project-spec.md` |
| 할일 관리 | `_core/docs/project-todo.md` |
| 작업 이력 | `_core/docs/project-log.md` |
| 세션 시작 | `_core/commands/session-start.md` |
| 세션 종료 | `_core/commands/session-end.md` |
| 세션 핸드오프 | `_core/commands/session-handoff.md` |
| 프로젝트 초기화 | `_core/commands/project-init.md` |
| 프로젝트 상태 | `_core/commands/project-status.md` |
| 프로젝트 업데이트 | `_core/commands/project-update.md` |
| 커밋 메시지 | `_core/commands/commit-message.md` |
