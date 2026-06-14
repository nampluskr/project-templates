# create_project.py: Copy a template to create a new project directory.

import argparse
import os
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")

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


def copy_template(src: str, dest: str) -> int:
    count = 0
    for dirpath, dirnames, filenames in os.walk(src):
        rel_dir = os.path.relpath(dirpath, src)
        target_dir = os.path.join(dest, rel_dir)
        os.makedirs(target_dir, exist_ok=True)
        for filename in filenames:
            src_file = os.path.join(dirpath, filename)
            dest_file = os.path.join(target_dir, filename)
            shutil.copy2(src_file, dest_file)
            count += 1
    return count


def find_placeholders(dest: str) -> list[tuple[str, list[str]]]:
    results = []
    for filename in PLACEHOLDER_FILES:
        path = os.path.join(dest, filename)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
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

    src = os.path.join(TEMPLATES_DIR, args.template)
    dest = os.path.join(args.dest, args.name)

    if not os.path.exists(src):
        print(f"오류: 템플릿을 찾을 수 없습니다 — {src}")
        raise SystemExit(1)

    if os.path.exists(dest):
        print(f"오류: 대상 경로가 이미 존재합니다 — {dest}")
        raise SystemExit(1)

    print(f"템플릿:  {args.template}")
    print(f"프로젝트: {args.name}")
    print(f"경로:    {dest}")
    print()

    os.makedirs(dest)
    count = copy_template(src, dest)
    print(f"완료: {count}개 파일 복사")

    placeholders = find_placeholders(dest)
    if placeholders:
        print("\n플레이스홀더 치환이 필요한 파일:")
        for path, tokens in placeholders:
            rel = os.path.relpath(path, dest)
            print(f"  {rel}  —  {', '.join(tokens)}")

    print(f"\n다음 단계: VS Code로 {dest}/ 를 열어 플레이스홀더를 치환하세요.")


if __name__ == "__main__":
    main()
