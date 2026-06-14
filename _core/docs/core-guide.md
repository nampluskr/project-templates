---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# core-guide.md

이 워크스페이스의 구조와 이용 방법을 설명한다.
사람이 참조하는 문서이다. 에이전트는 수정하지 않는다.

## 1. 워크스페이스 기능

이 레포(`project-templates`)는 재사용 가능한 프로젝트 워크스페이스 템플릿을 관리하는 소스 레포이다.

두 가지 역할을 동시에 수행한다.

| 역할 | 설명 |
|---|---|
| 템플릿 소스 레포 | `project-docs-template`, `project-wiki-template`, `project-coding-template` 저장 |
| 템플릿 관리 프로젝트 | 이 레포 자체를 운영하기 위한 `CLAUDE.md`, `_core/`, `_core/scripts/` 보유 |

루트 레벨 파일(`CLAUDE.md`, `AGENTS.md`, `_core/`)은 템플릿 레포 자체 운영용이다.
`templates/project-*-template/` 내부 파일이 새 프로젝트에 복사된다.

## 2. 워크스페이스 구조

```text
project-templates/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _core/               # 이 레포 자체 운영 파일
│   ├── rules/
│   ├── commands/
│   ├── docs/            # 구조 설명 및 운영 가이드
│   ├── sessions/        # 세션 핸드오프 문서
│   ├── scripts/         # 자동화 스크립트
│   └── refs/            # 참조 전용 문서
├── shared/              # 템플릿 공통 파일 원본 (SSOT)
│   └── _core/
│       ├── rules/
│       └── commands/
└── templates/           # 복사 가능한 프로젝트 템플릿
    ├── project-docs-template/
    ├── project-wiki-template/
    └── project-coding-template/
```

각 폴더의 관리 주체는 다음과 같다.

| 폴더 | 내용 | 관리 주체 |
|---|---|---|
| `_core/rules/` | 운영 규칙, 에이전트 행동 규칙, 마크다운 스타일 | 사람 |
| `_core/commands/` | 커스텀 명령어 정의 | 사람 |
| `_core/docs/` | 운영 가이드 | 사람 |
| `_core/sessions/` | 세션 핸드오프 문서 | 에이전트 |
| `_core/scripts/` | 자동화 스크립트 | 사람 |
| `_core/refs/` | 참조 전용 문서 (수정 금지) | — |
| `shared/` | 템플릿에 배포할 공통 파일 원본 | 사람 |
| `templates/` | 복사 가능한 프로젝트 템플릿 루트 | 사람 + 에이전트 |

## 3. 두 가지 `_core/` 구분

이 레포에는 `_core/` 가 두 곳에 존재한다. 혼동하지 않는다.

| 경로 | 역할 |
|---|---|
| `project-templates/_core/` | 이 레포 자체 운영 파일. 새 프로젝트에 복사되지 않음 |
| `shared/_core/` | 각 템플릿의 `_core/` 원본 (SSOT) |
| `templates/*/_core/` | `shared/_core/` 에서 동기화된 결과. 새 프로젝트 생성 시 복사됨 |

## 4. 두 가지 `AGENTS.md` / `CLAUDE.md` 구분

루트 레벨과 템플릿 레벨의 파일은 역할이 다르다.

| 경로 | 역할 |
|---|---|
| `project-templates/AGENTS.md` | 이 레포를 유지·관리할 때 사용하는 에이전트 규칙 |
| `templates/project-docs-template/AGENTS.md` | 새 docs 프로젝트 생성 시 복사되는 파일 |

`CLAUDE.md` 도 동일하다. 작업 대상을 항상 명확히 확인한다.

## 5. 사용 시나리오

### 5.1. 새 프로젝트 생성

```
new-project 실행
```

`_core/commands/new-project.md` 참조.

### 5.2. 공통 파일 수정 및 배포

`shared/` 에서 공통 파일을 수정한 후 각 템플릿으로 동기화한다.

```
sync-shared 실행
```

`_core/commands/sync-shared.md` 참조.

### 5.3. 템플릿 구조 수정

`templates/` 하위 특정 템플릿의 루트 구조를 수정한다.
수정 후 `_core/docs/template-guide.md` 를 갱신한다.

### 5.4. 세션 핸드오프

```
session-handoff 실행
```

`_core/commands/session-handoff.md` 참조.

## 6. 에이전트 작업 원칙

에이전트가 이 레포에서 작업할 때 따르는 원칙이다.

| 원칙 | 설명 |
|---|---|
| 작업 대상 명시 | 루트 운영 파일과 템플릿 파일을 혼동하지 않는다 |
| 파일 삭제 자제 | 명시적 요청 없이 파일을 삭제하지 않는다 |
| 템플릿은 얕게 유지 | `src/` 내부, `docs/` 내부 구조를 강제하지 않는다 |
| 구조 변경 후 문서 갱신 | 템플릿 구조 변경 후 `_core/docs/template-guide.md` 를 즉시 갱신한다 |
| 공통 파일은 shared에서 | `shared/` 를 수정하고 sync로 배포한다. 템플릿 `_core/` 를 직접 수정하지 않는다 |

## 7. 커밋 가이드

작업 완료 후 커밋 메시지 예시는 다음과 같다.

```text
Add project template type guide
Update shared project file policy
Refine docs template root structure
Sync shared files into templates
Add new project creation workflow
```

소규모 변경은 `main` 에 직접 커밋한다.
대규모 구조 변경은 별도 브랜치(`stage/...`)를 사용한다.

## 8. 설계 원칙

- 하나의 GitHub 레포가 모든 템플릿을 관리한다.
- 템플릿은 루트 1-depth 구조만 정의한다. 내부 상세 구조를 강제하지 않는다.
- `shared/` 가 공통 파일의 SSOT이다.
- 새 프로젝트는 이 레포와 독립된 Git 레포로 생성된다.
- 생성 후 프로젝트 내부 파일은 이 레포 범위 밖이다.
