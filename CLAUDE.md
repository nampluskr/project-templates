---
tags: [templates, agent-config]
created: 2026-06-14
updated: 2026-06-14
---

# CLAUDE.md

이 파일은 Claude Code가 이 워크스페이스를 다룰 때 따르는 진입점 지침이다.
상세 규칙은 `_core/` 를 참조한다.

## 1. 워크스페이스 기능

이 워크스페이스(`project-templates`)는 재사용 가능한 프로젝트 템플릿을 관리하는 소스 레포이다.
`templates/` 하위 3개 템플릿의 구조를 정의·유지하고, 템플릿을 복사하여 독립 Git 레포로 새 프로젝트를 생성하는 데 사용한다.

## 2. 워크스페이스 구조

```text
project-templates/
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── .gitignore
├── _core/               # 이 레포 자체 운영 파일
│   ├── rules/
│   ├── commands/
│   ├── docs/
│   ├── sessions/
│   └── refs/            # 참조 전용 문서
├── shared/              # 템플릿 공통 파일 원본 (SSOT)
│   └── _core/
│       ├── rules/
│       └── commands/
├── templates/           # 복사 가능한 프로젝트 템플릿
│   ├── project-docs-template/
│   ├── project-wiki-template/
│   └── project-coding-template/
├── guides/              # 사용·관리 가이드 문서
└── scripts/             # 자동화 스크립트
```

## 3. 템플릿 종류

각 템플릿의 용도는 다음과 같다.

| 템플릿 | 용도 |
|---|---|
| `project-docs-template` | 기술 가이드, 매뉴얼, 문서 작성 프로젝트 |
| `project-wiki-template` | 장기 지식 노트 + 최종 문서 프로젝트 |
| `project-coding-template` | Python 코드, 노트북, 실험, 문서 프로젝트 |

## 4. `_core/` 범위 및 참조 경로

이 레포의 `_core/` 에는 레포 자체 운영에 필요한 파일만 둔다.
템플릿 파일(`templates/`, `shared/`)은 `_core/` 범위 밖이다.

각 하위 폴더의 허용 파일 유형은 다음과 같다.

| 하위 폴더 | 허용 파일 유형 |
|---|---|
| `rules/` | 레포 운영 규칙, 에이전트 행동 규칙, 문서 작성 스타일, 템플릿 관리 규칙 |
| `commands/` | 레포 관리용 커스텀 커맨드 |
| `docs/` | 구조 설명 및 운영 가이드 |
| `sessions/` | 세션 핸드오프 문서 |
| `refs/` | 참조 전용 문서 (수정 금지) |

### 4.1. 참조 경로

각 운영 파일의 경로는 다음과 같다.

| 항목 | 경로 |
|---|---|
| 에이전트 행동 규칙 | `_core/rules/agent-rules.md` |
| 문서 작성 스타일 규칙 | `_core/rules/markdown-rules.md` |
| 템플릿 관리 규칙 | `_core/rules/template-rules.md` |
| 구조 설명 및 가이드 | `_core/docs/core-guide.md` |
| 공통 파일 동기화 커맨드 | `_core/commands/sync-shared.md` |
| 새 프로젝트 생성 커맨드 | `_core/commands/new-project.md` |
| 세션 핸드오프 커맨드 | `_core/commands/session-handoff.md` |

## 5. 핵심 행동 규칙

- 작업 전 반드시 `_core/rules/agent-rules.md` 와 `_core/rules/template-rules.md` 를 참조한다.
- 모든 마크다운 문서는 `_core/rules/markdown-rules.md` 를 따른다.
- `shared/_core/` 가 공통 파일의 SSOT이다. 템플릿별 `_core/` 를 직접 수정하지 않는다.
- 템플릿 구조 변경 후 `guides/` 내 해당 문서를 즉시 갱신한다.
- `_core/refs/` 파일은 참조 전용이다. 수정하지 않는다.
- 새 프로젝트 생성 후 해당 프로젝트 내부는 이 레포 범위 밖이다.

## 6. 하위 문서

### 6.1. 운영 문서

- [[core-guide]] — `_core/` 구조 설명 및 사용 시나리오

### 6.2. 규칙

- [[agent-rules]] — 에이전트 허용/금지 행동
- [[markdown-rules]] — 문서 작성 스타일
- [[template-rules]] — 템플릿 구조 및 관리 규칙

### 6.3. 커맨드

- [[sync-shared]] — 공통 파일 동기화
- [[new-project]] — 새 프로젝트 생성
- [[session-handoff]] — 세션 핸드오프
