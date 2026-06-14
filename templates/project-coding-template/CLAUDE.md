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
- **템플릿**: `project-coding-template`

## 2. 프로젝트 구조

```text
{{PROJECT_SLUG}}/
├── _core/        # 프로젝트 운영 파일
├── data/         # 데이터 (경로 또는 설명)
├── src/          # 소스 코드
├── scripts/      # 실행 스크립트
├── notebooks/    # Jupyter 노트북
├── tests/        # 테스트 코드
├── configs/      # 설정 파일
├── experiments/  # 실험 기록
├── docs/         # 프로젝트 문서
└── outputs/      # 결과물 (모델, 그래프, 예측 등)
```

## 3. 폴더 역할

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

## 4. 핵심 행동 규칙

- 작업 전 `_core/rules/agent-rules.md` 를 참조한다.
- 모든 마크다운 문서는 `_core/rules/markdown-rules.md` 를 따른다.
- 루트 폴더 구조는 변경하지 않는다.

## 5. 참조 경로

| 항목 | 경로 |
|---|---|
| 에이전트 규칙 | `_core/rules/agent-rules.md` |
| 마크다운 규칙 | `_core/rules/markdown-rules.md` |
| 프로젝트 가이드 | `_core/docs/project-guide.md` |
| 작업 이력 | `_core/docs/project-log.md` |
| 세션 핸드오프 | `_core/commands/session-handoff.md` |
