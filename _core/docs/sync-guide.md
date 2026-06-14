---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# sync-guide.md

`shared/` 와 `templates/*/` 간 동기화 구조, 원칙, 절차를 설명한다.

## 1. 동기화 구조

이 레포에는 `_core/` 가 두 맥락에서 존재한다.

| 경로 | 역할 |
|---|---|
| `project-templates/_core/` | 이 레포 자체 운영 파일. 새 프로젝트에 복사되지 않음 |
| `shared/` | 각 템플릿의 공통 파일 원본 (SSOT) |
| `templates/*/` | `shared/` 에서 동기화된 결과. 새 프로젝트 생성 시 복사됨 |

동기화 방향은 단방향이다.

```text
shared/ → templates/project-docs-template/
        → templates/project-wiki-template/
        → templates/project-coding-template/
```

## 2. 동기화 대상

`shared/` 아래 모든 파일이 동기화 대상이다.

| 소스 | 대상 |
|---|---|
| `shared/_core/rules/` | `templates/*/_core/rules/` |
| `shared/_core/commands/` | `templates/*/_core/commands/` |
| `shared/README.md` | `templates/*/README.md` |
| `shared/.gitignore` | `templates/*/.gitignore` |
| `shared/_project/` | `templates/*/_project/` |

`shared/` 에 파일이나 폴더를 추가하면 다음 sync 실행 시 자동으로 반영된다.

## 3. 동기화 제외 대상

다음 파일은 템플릿별로 독립 관리한다. `shared/` 에 두지 않는다.

| 파일 | 이유 |
|---|---|
| `AGENTS.md` | 템플릿 유형마다 내용이 다름 |
| `CLAUDE.md` | 템플릿 유형마다 내용이 다름 |
| `wiki/`, `src/`, `pyproject.toml` 등 | 템플릿 전용 구조 |

## 4. 동기화 원칙

- `shared/` 를 수정한 후 `_core/scripts/sync_shared.py` 로 각 템플릿에 배포한다.
- 배포는 덮어쓰기 방식이다. `shared/` 가 SSOT이다.
- 템플릿별 `_core/` 에 추가된 전용 파일은 삭제하지 않는다.
- 배포 전 반드시 dry-run으로 변경 대상을 확인한다.
- 템플릿별 공통 파일을 직접 수정하지 않는다.

## 5. 동기화 절차

공통 파일 수정 후 동기화 절차는 다음과 같다.

1. `shared/` 에서 파일 수정
2. `sync-shared` 커맨드 실행 (dry-run)
3. 변경 대상 확인
4. `sync-shared` 커맨드 실행 (`--apply`)
5. `templates/*/` 결과 검증

상세 절차는 `_core/commands/sync-shared.md` 를 참조한다.

## 6. 스크립트

동기화 스크립트 경로와 사용법은 다음과 같다.

```bash
# 변경 예정 목록 확인
python _core/scripts/sync_shared.py --dry-run

# 실제 동기화 실행
python _core/scripts/sync_shared.py --apply
```

스크립트는 `shared/` 아래 모든 파일을 대상으로 동작한다.

## 7. 커밋

동기화 후 커밋 예시는 다음과 같다.

```bash
git add templates/
git commit -m "Sync shared files into templates"
git push origin main
```

## 8. 템플릿별 전용 파일

각 템플릿의 `_core/` 에는 공통 파일 외에 템플릿 전용 파일이 추가될 수 있다.
전용 파일은 `shared/` 에 포함하지 않으며 동기화 시 삭제되지 않는다.

| 템플릿 | 전용 파일 예시 |
|---|---|
| `project-docs-template` | (현재 없음) |
| `project-wiki-template` | (현재 없음) |
| `project-coding-template` | (현재 없음) |
