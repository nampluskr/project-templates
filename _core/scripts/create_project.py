"""
create_project.py

템플릿을 복사하여 새 프로젝트를 생성한다.

사용법:
    python _core/scripts/create_project.py \\
        --template project-docs-template \\
        --name new-project-name \\
        --dest /mnt/d/projects/nampluskr/00_review
"""

import argparse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"

TEMPLATES = [
    "project-docs-template",
    "project-wiki-template",
    "project-coding-template",
]

PLACEHOLDER_FILES = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
]


def copy_template(src: Path, dest: Path) -> int:
    count = 0
    for item in src.rglob("*"):
        rel = item.relative_to(src)
        target = dest / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            count += 1
    return count


def find_placeholders(dest: Path) -> list[tuple[Path, list[str]]]:
    results = []
    for filename in PLACEHOLDER_FILES:
        path = dest / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        found = [p for p in ["{{PROJECT_NAME}}", "{{PROJECT_SLUG}}", "{{PROJECT_DESCRIPTION}}"] if p in text]
        if found:
            results.append((path, found))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="템플릿에서 새 프로젝트 생성")
    parser.add_argument("--template", required=True, choices=TEMPLATES, help="사용할 템플릿")
    parser.add_argument("--name", required=True, help="프로젝트명 (소문자 + 하이픈)")
    parser.add_argument("--dest", required=True, help="생성할 상위 디렉토리 경로")
    args = parser.parse_args()

    src = TEMPLATES_DIR / args.template
    dest = Path(args.dest) / args.name

    if not src.exists():
        print(f"오류: 템플릿을 찾을 수 없습니다 — {src}")
        raise SystemExit(1)

    if dest.exists():
        print(f"오류: 대상 경로가 이미 존재합니다 — {dest}")
        raise SystemExit(1)

    print(f"템플릿:  {args.template}")
    print(f"프로젝트: {args.name}")
    print(f"경로:    {dest}")
    print()

    dest.mkdir(parents=True)
    count = copy_template(src, dest)
    print(f"완료: {count}개 파일 복사")

    placeholders = find_placeholders(dest)
    if placeholders:
        print("\n플레이스홀더 치환이 필요한 파일:")
        for path, tokens in placeholders:
            rel = path.relative_to(dest)
            print(f"  {rel}  —  {', '.join(tokens)}")

    print(f"\n다음 단계: VS Code로 {dest}/ 를 열어 플레이스홀더를 치환하세요.")


if __name__ == "__main__":
    main()
