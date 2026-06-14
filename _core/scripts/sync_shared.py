# sync_shared.py: Sync common files from shared/ to each template directory.

import argparse
import os
import shutil

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHARED_DIR = os.path.join(REPO_ROOT, "shared")
TEMPLATES_DIR = os.path.join(REPO_ROOT, "templates")

TEMPLATES = [
    "project-docs-template",
    "project-wiki-template",
    "project-coding-template",
]


def get_shared_files() -> list[str]:
    result = []
    for dirpath, _, filenames in os.walk(SHARED_DIR):
        for filename in filenames:
            result.append(os.path.join(dirpath, filename))
    return result


def sync(dry_run: bool) -> None:
    shared_files = get_shared_files()

    if not shared_files:
        print("동기화할 파일이 없습니다.")
        return

    synced = 0

    for template in TEMPLATES:
        template_root = os.path.join(TEMPLATES_DIR, template)

        for src in shared_files:
            rel = os.path.relpath(src, SHARED_DIR)
            dest = os.path.join(template_root, rel)

            if os.path.exists(dest):
                with open(src, encoding="utf-8") as f:
                    src_text = f.read()
                with open(dest, encoding="utf-8") as f:
                    dest_text = f.read()
                if src_text == dest_text:
                    continue
                status = "수정"
            else:
                status = "신규"

            print(f"[{status}] {template}/{rel}")

            if not dry_run:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(src, dest)

            synced += 1

    if synced == 0:
        print("모든 파일이 최신 상태입니다.")
        return

    if dry_run:
        print(f"\ndry-run: {synced}개 파일 변경 예정 (실제 적용하려면 --apply 사용)")
    else:
        print(f"\n완료: {synced}개 파일 동기화")
        print(f"대상 템플릿: {', '.join(TEMPLATES)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="shared/ → templates/*/ 동기화")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="변경 예정 파일 목록만 출력")
    group.add_argument("--apply", action="store_true", help="실제 동기화 실행")
    args = parser.parse_args()

    sync(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
