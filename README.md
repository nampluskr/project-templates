---
tags: [templates]
created: 2026-06-14
updated: 2026-06-14
---

# project-templates

재사용 가능한 프로젝트 워크스페이스 템플릿을 관리하는 소스 레포이다.

이 레포는 실제 작업 프로젝트가 아니다. 새 프로젝트를 생성할 때 복사할 템플릿 구조를 정의하고 유지한다.

## 1. 템플릿 종류

세 가지 템플릿을 제공한다.

| 템플릿 | 용도 |
|---|---|
| `project-docs-template` | 기술 가이드, 매뉴얼, 문서 작성 프로젝트 |
| `project-wiki-template` | 장기 지식 노트 + 최종 문서 프로젝트 |
| `project-coding-template` | Python 코드, 노트북, 실험, 문서 프로젝트 |

## 2. 레포 구조

```text
project-templates/
├── README.md
├── CLAUDE.md            # Claude Code 운영 지침
├── AGENTS.md            # Codex 운영 지침
├── .gitignore
├── _core/               # 이 레포 자체 운영 파일
├── shared/              # 템플릿 공통 파일 원본
└── templates/           # 복사 가능한 프로젝트 템플릿
```

## 3. 사용 방법

새 프로젝트를 생성할 때는 해당 템플릿 폴더를 새 Git 레포로 복사한다.

```bash
rsync -av templates/project-docs-template/ /path/to/new-project/
```

복사 후 `{{PROJECT_NAME}}`, `{{PROJECT_SLUG}}`, `{{PROJECT_DESCRIPTION}}` 플레이스홀더를 치환한다.
생성된 프로젝트는 이 레포와 독립적으로 관리된다.

## 4. 운영 원칙

- 각 템플릿은 루트 1-depth 구조만 정의한다. 내부 상세 구조는 강제하지 않는다.
- 템플릿 간 공통 파일은 `shared/_core/` 에서 관리하고 각 템플릿으로 배포한다.
- 생성된 프로젝트의 내부 파일은 이 레포 범위 밖이다.
