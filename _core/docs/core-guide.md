---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# core-guide.md

이 워크스페이스의 구조와 이용 방법을 설명한다.
사람이 참조하는 문서이다. 에이전트는 수정하지 않는다.

## 1. 워크스페이스 구조

이 레포(`project-templates`)는 재사용 가능한 프로젝트 워크스페이스 템플릿을 관리하는 소스 레포이다.

```text
project-templates/
├── README.md
├── AGENTS.md
├── CLAUDE.md
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
└── scripts/             # 자동화 스크립트
```

각 폴더의 관리 주체는 다음과 같다.

| 폴더 | 내용 | 관리 주체 |
|---|---|---|
| `_core/rules/` | 운영 규칙, 에이전트 행동 규칙, 마크다운 스타일 | 사람 |
| `_core/commands/` | 커스텀 명령어 정의 | 사람 |
| `_core/docs/` | 운영 가이드 | 사람 |
| `_core/sessions/` | 세션 핸드오프 문서 | 에이전트 |
| `_core/refs/` | 참조 전용 문서 (수정 금지) | — |
| `shared/_core/` | 템플릿에 배포할 공통 `_core/` 원본 | 사람 |
| `templates/` | 복사 가능한 프로젝트 템플릿 루트 | 사람 + 에이전트 |
| `scripts/` | 자동화 스크립트 | 사람 |

## 2. 두 가지 `_core/` 구분

이 레포에는 `_core/` 가 두 곳에 존재한다. 혼동하지 않는다.

| 경로 | 역할 |
|---|---|
| `project-templates/_core/` | 이 레포 자체 운영 파일. 새 프로젝트에 복사되지 않음 |
| `shared/_core/` | 각 템플릿의 `_core/` 원본. 동기화를 통해 `templates/*/_core/` 로 배포됨 |
| `templates/*/_core/` | 새 프로젝트 생성 시 복사되는 `_core/` |

## 3. 사용 시나리오

### 3.1. 새 프로젝트 생성

```
new-project 실행
```

`_core/commands/new-project.md` 참조.

### 3.2. 공통 파일 수정 및 배포

`shared/_core/` 에서 공통 파일을 수정한 후 각 템플릿으로 동기화한다.

```
sync-shared 실행
```

`_core/commands/sync-shared.md` 참조.

### 3.3. 템플릿 구조 수정

`templates/` 하위 특정 템플릿의 루트 구조를 수정한다.
수정 후 `_core/docs/` 내 해당 문서를 갱신한다.

### 3.4. 세션 핸드오프

```
session-handoff 실행
```

`_core/commands/session-handoff.md` 참조.

## 4. 설계 원칙

- 템플릿은 루트 1-depth 구조만 정의한다. 내부 상세 구조를 강제하지 않는다.
- `shared/_core/` 가 공통 파일의 SSOT이다.
- 새 프로젝트는 이 레포와 독립된 Git 레포로 생성된다.
- 생성 후 프로젝트 내부 파일은 이 레포 범위 밖이다.
