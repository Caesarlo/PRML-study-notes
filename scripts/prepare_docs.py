from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / ".mkdocs-src"

FILES = [
    "index.md",
]

DIRECTORIES = [
    "Ch01 - Introduction",
    "javascripts",
]


def copy_file(relative_path: str) -> None:
    source = ROOT / relative_path
    target = DOCS_DIR / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_directory(relative_path: str) -> None:
    source = ROOT / relative_path
    target = DOCS_DIR / relative_path
    if source.exists():
        shutil.copytree(source, target)


def main() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)

    DOCS_DIR.mkdir(parents=True)

    for file_path in FILES:
        copy_file(file_path)

    for directory_path in DIRECTORIES:
        copy_directory(directory_path)


if __name__ == "__main__":
    main()
