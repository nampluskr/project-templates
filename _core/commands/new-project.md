---
tags: [templates, commands]
created: 2026-06-14
updated: 2026-06-14
---

# 커스텀 명령어: `new-project` / `새 프로젝트 생성`

`new-project 실행` 또는 `@new-project.md 실행`으로 호출한다.
템플릿에서 새 프로젝트를 생성하는 절차를 안내한다.

## 1. 실행 절차

### Step 1. 정보 확인

사용자에게 다음 정보를 확인한다.

```
템플릿:      project-docs-template | project-wiki-template | project-coding-template
프로젝트명:  {project-name}  (소문자 + 하이픈)
저장 경로:   {workspace}/{account}/00_review/{project-name}
GitHub 레포: nampluskr/{project-name}  (생성 여부 확인)
```

### Step 2. 스크립트 실행

```bash
python _core/scripts/create_project.py \
  --template project-docs-template \
  --name {project-name} \
  --dest /mnt/d/projects/{account}/00_review/{project-name}
```

### Step 3. 플레이스홀더 치환 확인

생성된 프로젝트에서 치환이 필요한 파일 목록을 제시한다.

```
README.md          — {{PROJECT_NAME}}, {{PROJECT_DESCRIPTION}}
CLAUDE.md          — {{PROJECT_NAME}}
_core/docs/project-guide.md  — {{PROJECT_NAME}}, {{PROJECT_DESCRIPTION}}
```

### Step 4. 결과 보고

```
완료: {project-name} 생성
경로: {dest}/
템플릿: {template}
다음 단계: VS Code로 {dest}/ 를 열어 플레이스홀더를 치환하세요.
```

## 2. 템플릿 선택 기준

사용할 템플릿을 선택하는 기준은 다음과 같다.

| 상황 | 권장 템플릿 |
|---|---|
| 기술 가이드, 매뉴얼 작성 | `project-docs-template` |
| 장기 지식 노트 + 최종 문서 | `project-wiki-template` |
| Python 코드, 노트북, 실험 관리 | `project-coding-template` |
