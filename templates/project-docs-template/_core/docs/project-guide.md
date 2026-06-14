---
tags: [project, docs]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# project-guide.md

이 프로젝트의 구조와 목적을 설명한다.
사용자가 참조하는 문서이다. 에이전트는 수정하지 않는다.

## 1. 프로젝트 개요

- **이름**: {{PROJECT_NAME}}
- **목적**: {{PROJECT_DESCRIPTION}}
- **템플릿**: `project-docs-template`

## 2. 폴더 구조

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `inbox/` | 아직 분류하지 않은 임시 입력 자료 |
| `sources/` | 정리된 참고 자료 |
| `docs/` | 최종 문서 |
| `outputs/` | 생성물, 빌드 결과, 내보내기 |

## 3. 자료 흐름

자료는 다음 순서로 이동한다.

```
inbox/ → sources/ → docs/ → outputs/
```

## 4. _core/ 구조

```text
_core/
├── rules/
│   ├── agent-rules.md
│   ├── docs-rules.md
│   └── python-rules.md
├── commands/
│   ├── session-start.md
│   ├── session-end.md
│   ├── session-handoff.md
│   ├── project-init.md
│   ├── project-status.md
│   ├── project-update.md
│   └── commit-message.md
├── docs/
│   ├── project-guide.md   # 이 파일
│   ├── project-spec.md
│   ├── project-todo.md
│   ├── project-log.md
│   └── subject-guide.md
└── sessions/
```
