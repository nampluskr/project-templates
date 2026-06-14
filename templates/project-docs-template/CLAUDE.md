---
tags: [project, agent-config]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# CLAUDE.md — {{PROJECT_NAME}}

이 파일은 Claude Code가 이 프로젝트를 다룰 때 따르는 진입점 지침이다.
상세 규칙은 `_core/` 를 참조한다.

## 1. 프로젝트 개요

- **이름**: {{PROJECT_NAME}}
- **목적**: {{PROJECT_DESCRIPTION}}
- **템플릿**: `project-docs-template`

## 2. 프로젝트 구조

```text
{{PROJECT_SLUG}}/
├── _core/        # 프로젝트 운영 파일
├── inbox/        # 미분류 입력 자료
├── sources/      # 정리된 참고 자료
├── docs/         # 최종 문서
└── outputs/      # 생성물, 빌드 결과
```

## 3. 폴더 역할

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 아직 분류하지 않은 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 빌드 결과, 내보내기 |

## 4. 핵심 행동 규칙

- 작업 전 `_core/rules/agent-rules.md` 를 참조한다.
- 마크다운 문서 작성·수정 시 `_core/rules/docs-rules.md` 를 따른다.
- Python 스크립트 작성·수정 시 `_core/rules/python-rules.md` 를 따른다.
- 루트 폴더 구조는 변경하지 않는다.

## 5. 참조 경로

| 항목 | 경로 |
|---|---|
| 에이전트 규칙 | `_core/rules/agent-rules.md` |
| 마크다운 규칙 | `_core/rules/docs-rules.md` |
| Python 규칙 | `_core/rules/python-rules.md` |
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
