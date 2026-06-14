---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# new-project-guide.md

템플릿을 복사하여 새 독립 Git 레포를 만드는 절차를 설명한다.

## 1. 전제 조건

새 프로젝트 생성 전 다음을 확인한다.

- 이 레포(`project-templates`)가 로컬에 클론되어 있음
- 사용할 템플릿이 `templates/` 하위에 존재함
- 새 프로젝트 이름이 결정됨
- 새 GitHub 레포가 생성됨 (빈 레포, README 초기화 안 함)

## 2. 절차

### 2.1. 빈 GitHub 레포 생성

GitHub에서 새 레포를 생성한다.

권장 설정은 다음과 같다.

| 항목 | 값 |
|---|---|
| Repository name | `new-project-name` |
| Initialize README | No |
| Add .gitignore | No |
| Add license | No |

### 2.2. 빈 레포 클론

```bash
cd /mnt/d/projects/nampluskr/00_review
git clone https://github.com/nampluskr/new-project-name.git
```

### 2.3. 템플릿 복사

WSL에서 `rsync` 를 사용한다.

```bash
rsync -av \
  /mnt/d/projects/projects-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-project-name/
```

또는 `scripts/create_project.py` 를 사용한다.

```bash
python scripts/create_project.py \
  --template project-docs-template \
  --name new-project-name \
  --dest /mnt/d/projects/nampluskr/00_review
```

상세 절차는 `_core/commands/new-project.md` 를 참조한다.

### 2.4. 플레이스홀더 치환

복사 후 아래 플레이스홀더를 실제 값으로 교체한다.

| 플레이스홀더 | 내용 |
|---|---|
| `{{PROJECT_NAME}}` | 프로젝트 표시 이름 |
| `{{PROJECT_SLUG}}` | 레포명 (kebab-case) |
| `{{PROJECT_DESCRIPTION}}` | 프로젝트 한 줄 설명 |

수정 대상 파일은 다음과 같다.

```text
README.md
AGENTS.md
CLAUDE.md
```

### 2.5. 첫 커밋 및 푸시

```bash
cd new-project-name
git add .
git commit -m "Initialize project from project-docs-template"
git push origin main
```

## 3. 생성 후 원칙

새 프로젝트 생성 후 지켜야 할 원칙은 다음과 같다.

- 새 프로젝트는 이 레포와 독립된 Git 레포이다.
- 생성 후 프로젝트 내부 파일은 이 레포 범위 밖이다.
- 이 레포의 템플릿 변경은 기존 프로젝트에 자동 반영되지 않는다.
- 프로젝트가 안정화되면 `00_review/` 에서 `20_active/` 로 이동한다.
