---
tags: [project, agent-config]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# AGENTS.md — {{PROJECT_NAME}}

이 파일은 Codex가 이 프로젝트를 다룰 때 따르는 진입점 지침이다.
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

## 3. 핵심 행동 규칙

- 작업 전 `_core/rules/agent-rules.md` 를 참조한다.
- 모든 마크다운 문서는 `_core/rules/markdown-rules.md` 를 따른다.
- 루트 폴더 구조는 변경하지 않는다.

## 4. 응답 스타일

- 한국어 경어체로 응답한다.
- 변경한 파일과 결과를 간단히 요약한다.
