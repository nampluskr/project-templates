"""
sync_shared.py

shared/_core/ 의 공통 파일을 templates/*/_core/ 로 동기화한다.

사용법:
    python _core/scripts/sync_shared.py --dry-run
    python _core/scripts/sync_shared.py --apply
"""

import argparse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
SHARED_CORE = REPO_ROOT / "shared" / "_core"
TEMPLATES_DIR = REPO_ROOT / "templates"

TEMPLATES = [
    "project-docs-template",
    "project-wiki-template",
    "project-coding-template",
]


def get_shared_files() -> list[Path]:
    return [p for p in SHARED_CORE.rglob("*") if p.is_file()]


def sync(dry_run: bool) -> None:
    shared_files = get_shared_files()

    if not shared_files:
        print("동기화할 파일이 없습니다.")
        return

    synced = 0

    for template in TEMPLATES:
        template_core = TEMPLATES_DIR / template / "_core"

        for src in shared_files:
            rel = src.relative_to(SHARED_CORE)
            dest = template_core / rel

            if dest.exists():
                src_text = src.read_text(encoding="utf-8")
                dest_text = dest.read_text(encoding="utf-8")
                if src_text == dest_text:
                    continue
                status = "수정"
            else:
                status = "신규"

            print(f"[{status}] {template}/_core/{rel}")

            if not dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
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
    parser = argparse.ArgumentParser(description="shared/_core/ → templates/*/_core/ 동기화")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true", help="변경 예정 파일 목록만 출력")
    group.add_argument("--apply", action="store_true", help="실제 동기화 실행")
    args = parser.parse_args()

    sync(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
