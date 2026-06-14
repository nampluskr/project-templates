---
tags: [templates, docs]
created: 2026-06-14
updated: 2026-06-14
---

# new-project-guide.md

템플릿을 복사하여 새 독립 Git 레포를 만드는 절차를 설명한다.

## 1. 핵심 개념

```text
project-templates/templates/project-docs-template/  (소스)
    ↓ 복사
nampluskr/new-docs-project  (독립 GitHub 레포)
```

생성 후 새 프로젝트는 이 레포와 완전히 독립된다.
이 레포의 템플릿 변경은 기존 프로젝트에 자동 반영되지 않는다.

## 2. 전제 조건

새 프로젝트 생성 전 다음을 확인한다.

- 이 레포(`project-templates`)가 로컬에 클론되어 있음
- 템플릿이 동기화된 최신 상태임 (확실하지 않으면 `sync-shared` 실행)
- 새 프로젝트 이름이 결정됨
- 템플릿 종류가 결정됨

## 3. Step 1: 빈 GitHub 레포 생성

GitHub에서 새 레포를 생성한다. 초기화 옵션은 모두 비운다.

| 항목 | 값 |
|---|---|
| Repository name | 예: `new-docs-project` |
| Visibility | Private 또는 Public |
| Initialize README | No |
| Add .gitignore | No |
| Add license | No |

## 4. Step 2: 빈 레포 클론

### WSL

```bash
cd /mnt/d/projects/nampluskr/00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

### Windows PowerShell

```powershell
cd D:\projects\nampluskr\00_review
git clone https://github.com/nampluskr/new-docs-project.git
cd new-docs-project
```

처음에는 `00_review/` 에 생성하고, 실제 작업 프로젝트가 되면 `20_active/` 로 이동한다.

## 5. Step 3: 템플릿 복사

### WSL (권장)

```bash
rsync -av \
  /mnt/d/projects/projects-templates/templates/project-docs-template/ \
  /mnt/d/projects/nampluskr/00_review/new-docs-project/
```

### Windows PowerShell

```powershell
robocopy `
  D:\projects\projects-templates\templates\project-docs-template `
  D:\projects\nampluskr\00_review\new-docs-project `
  /E
```

`project-docs-template` 자리에 `project-wiki-template` 또는 `project-coding-template` 을 사용한다.

## 6. Step 4: 복사 결과 확인

복사 후 예상 구조가 존재하는지 확인한다.

`project-docs-template` 기준:

```text
new-docs-project/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── .gitignore
├── _core/
├── inbox/
├── sources/
├── docs/
└── outputs/
```

`project-wiki-template` 은 `wiki/` 가 추가된다.
`project-coding-template` 은 `pyproject.toml`, `src/`, `notebooks/` 등이 추가된다.

## 7. Step 5: 플레이스홀더 치환

복사 후 아래 플레이스홀더를 실제 값으로 교체한다.

| 플레이스홀더 | 내용 |
|---|---|
| `{{PROJECT_NAME}}` | 프로젝트 표시 이름 |
| `{{PROJECT_SLUG}}` | 레포명 (kebab-case) |
| `{{PROJECT_DESCRIPTION}}` | 프로젝트 한 줄 설명 |
| `{{AUTHOR}}` | 작성자 |

수정 대상 파일은 다음과 같다.

```text
README.md
AGENTS.md
CLAUDE.md
_core/docs/project-guide.md
_core/docs/project-log.md
```

## 8. Step 6: VS Code에서 열기

새 프로젝트 루트를 열어야 한다. `project-templates` 루트를 열지 않는다.

```bash
cd /mnt/d/projects/nampluskr/00_review/new-docs-project
code .
```

## 9. Step 7: 첫 커밋 및 푸시

```bash
git add .
git commit -m "Initialize project from project-docs-template"
git branch -M main
git push -u origin main
```

## 10. Step 8: 프로젝트 이동

프로젝트가 안정화되면 `00_review/` 에서 `20_active/` 로 이동한다.

```text
D:/projects/nampluskr/00_review/new-docs-project
→ D:/projects/nampluskr/20_active/new-docs-project
```

이동 후 git remote 설정은 그대로 유지된다. 이동 후 확인한다.

```bash
git remote -v
git status
```

## 11. 템플릿 업데이트 정책

이 레포의 템플릿이 변경되어도 기존 프로젝트에는 자동 반영되지 않는다.

기존 프로젝트에 적용이 필요한 경우 선택적으로 진행한다.

안전하게 업데이트 가능한 파일:

```text
AGENTS.md
CLAUDE.md
_core/rules/
_core/commands/
```

덮어쓰지 않아야 할 파일 (프로젝트 고유 내용 포함):

```text
README.md
_core/docs/project-guide.md
_core/docs/project-log.md
docs/
src/
```

## 12. 생성 후 원칙

- 새 프로젝트는 이 레포와 독립된 Git 레포이다.
- 생성 후 프로젝트 내부 파일은 이 레포 범위 밖이다.
- 이 레포에서 새 프로젝트 내부를 수정하지 않는다.
