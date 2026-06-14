---
tags: [templates, commands]
created: 2026-06-14
updated: 2026-06-14
---

# 커스텀 명령어: `sync-shared` / `공통 파일 동기화`

`sync-shared 실행` 또는 `@sync-shared.md 실행`으로 호출한다.
`shared/` 의 공통 파일을 각 템플릿 루트로 동기화한다.

## 1. 실행 절차

### Step 1. dry-run 실행

```bash
python _core/scripts/sync_shared.py --dry-run
```

변경 예정 파일 목록을 사용자에게 보고한다.

### Step 2. 사용자 승인

dry-run 결과를 확인하고 실행 여부를 확인받는다.

### Step 3. 실제 동기화

```bash
python _core/scripts/sync_shared.py --apply
```

### Step 4. 결과 보고

```
완료: {N}개 파일 동기화
대상 템플릿: project-docs-template, project-wiki-template, project-coding-template
```

## 2. 동기화 범위

`shared/` 아래 모든 파일이 동기화 대상이다.

| 소스 | 대상 |
|---|---|
| `shared/_core/` | `templates/*/_core/` |
| `shared/README.md` | `templates/*/README.md` |
| `shared/.gitignore` | `templates/*/.gitignore` |
| `shared/_project/` | `templates/*/_project/` |

`shared/` 에 파일/폴더를 추가하면 다음 sync 실행 시 자동으로 반영된다.

## 3. 주의사항

- 템플릿별 전용 파일(`AGENTS.md`, `CLAUDE.md` 등)은 `shared/` 에 두지 않는다.
- 템플릿별로 추가된 고유 파일은 sync로 삭제되지 않는다.
- 동기화는 덮어쓰기 방식이다. `shared/` 가 SSOT이다.
