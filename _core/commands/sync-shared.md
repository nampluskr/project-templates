---
tags: [templates, commands]
created: 2026-06-14
updated: 2026-06-14
---

# 커스텀 명령어: `sync-shared` / `공통 파일 동기화`

`sync-shared 실행` 또는 `@sync-shared.md 실행`으로 호출한다.
`shared/_core/` 의 공통 파일을 각 템플릿의 `_core/` 로 동기화한다.

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

동기화 대상과 제외 대상은 다음과 같다.

| 동기화 (`shared/_core/` → `templates/*/_core/`) | 제외 |
|---|---|
| `rules/markdown-rules.md` | 템플릿별 전용 파일 |
| `rules/agent-rules.md` | |
| `commands/session-handoff.md` | |

## 3. 주의사항

- 템플릿별 `_core/` 에 추가된 전용 파일은 삭제하지 않는다.
- `shared/_core/` 에 없는 파일은 건드리지 않는다.
- 동기화는 덮어쓰기 방식이다. `shared/_core/` 가 SSOT이다.
