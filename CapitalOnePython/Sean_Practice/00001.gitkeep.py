from __future__ import annotations

import argparse
from pathlib import Path
from typing import Annotated , Optional

def is_empty_dir(path: Path) -> bool:
    """ Check if a directory is empty (no files or subdirectories). """
    return not any(path.iterdir())

def add_gitkeep_to_empty_dirs(root_path: Path) -> int:
    """ Recursively traverse directories starting from root_path. """
    count: int = 0
    for dir_path in root_path.rglob("*"):
        if not dir_path.is_dir():
            continue
        if is_empty_dir(dir_path):
            gitkeep_path: Path = dir_path / ".gitkeep"
            if not gitkeep_path.exists():
                gitkeep_path.touch()
                count += 1
    return count

def main()->None:
    """ CLI entry Point with argparse """
    parser = argparse.ArgumentParser(description = "Add .gitkeep to empty directories in a tree (idempotent).")
    parser.add_argument("--path"
                        , type = Path
                        , required = True
                        , help = "Root directory path to traverse (e.g., C:\\pyproj\\Study\\CapitalOnePython\\Part2_PowerDay)")
    args: Annotated[argparse.Namespace, "Parsed args"] = parser.parse_args()

    
    
    root: Path = args.path.resolve()
    print(root)
    if not root.is_dir():
        raise ValueError(f"Provided path is not a directory: {root}")
    
    added = add_gitkeep_to_empty_dirs(root)
    print(f"Processed {root}. Added {added} .gitkeep files.")




if __name__ == "__main__":
    main()