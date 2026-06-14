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
- **템플릿**: `project-coding-template`

## 2. 폴더 구조

각 폴더의 역할은 다음과 같다.

| 폴더 | 역할 |
|---|---|
| `_core/` | 프로젝트 운영 규칙, 커맨드, 가이드, 세션 |
| `data/` | 데이터 경로 또는 설명 |
| `src/` | 소스 코드 루트 |
| `scripts/` | 실행 가능한 스크립트 |
| `notebooks/` | Jupyter 노트북 |
| `tests/` | 테스트 코드 |
| `configs/` | 설정 파일 |
| `experiments/` | 실험 기록 및 실행 메타데이터 |
| `docs/` | 프로젝트 문서 |
| `outputs/` | 모델, 그래프, 예측, 내보내기 결과 |

## 4. _core/ 구조

```text
_core/
├── rules/
│   ├── agent-rules.md
│   ├── docs-rules.md
│   ├── python-rules.md
│   └── coding-rules.md    # coding-template 전용
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
│   ├── subject-guide.md
│   └── coding-guide.md    # coding-template 전용
└── sessions/
```
