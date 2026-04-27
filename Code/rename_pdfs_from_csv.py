"""Rename PDF files in a folder based on a two-column CSV file.

The first column contains the current filename and the second column contains
the desired target filename.
"""

from __future__ import annotations

import argparse
import csv
import uuid
from pathlib import Path

from pdf_workflow_core import iter_pdf_files


DEFAULT_INPUT_DIR = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\Kurztests\Kurztest_3_v2"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rename PDFs in a folder using a CSV with current and target filenames.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/rename_pdfs_from_csv.py
  python Code/rename_pdfs_from_csv.py "C:/Data/PDFs" --apply
  python Code/rename_pdfs_from_csv.py "C:/Data/PDFs" --csv-file "C:/Data/PDFs/pdf_names.csv" --apply
""",
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        metavar="INPUT_DIR",
        help=f"Folder containing the PDF files. Defaults to {DEFAULT_INPUT_DIR}.",
    )
    parser.add_argument(
        "--csv-file",
        type=Path,
        default=None,
        metavar="CSV_FILE",
        help="CSV file with columns current_name and new_name. Defaults to pdf_names.csv inside the input directory.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rename files. Without this flag, the script only shows a preview.",
    )
    return parser.parse_args()


def normalize_pdf_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        return ""

    path = Path(cleaned)
    if cleaned.lower().endswith(".pdf"):
        return path.name
    return f"{path.name}.pdf"


def load_rename_pairs(csv_file: Path, input_dir: Path) -> list[tuple[Path, Path]]:
    with csv_file.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "current_name" not in reader.fieldnames or "new_name" not in reader.fieldnames:
            raise SystemExit("CSV file must contain the columns current_name and new_name.")

        pairs: list[tuple[Path, Path]] = []
        for row_number, row in enumerate(reader, start=2):
            current_name = normalize_pdf_name((row.get("current_name") or ""))
            new_name = normalize_pdf_name((row.get("new_name") or ""))
            if not current_name or not new_name:
                continue

            source_path = (input_dir / current_name).resolve()
            target_path = (input_dir / new_name).resolve()
            pairs.append((source_path, target_path))

    return pairs


def make_temp_path(source_path: Path) -> Path:
    temp_name = f".__rename_tmp__{uuid.uuid4().hex}{source_path.suffix}"
    return source_path.with_name(temp_name)


def safe_rename(source_path: Path, target_path: Path) -> None:
    if source_path == target_path:
        return

    temp_path = make_temp_path(source_path)
    while temp_path.exists():
        temp_path = make_temp_path(source_path)

    source_path.rename(temp_path)
    temp_path.rename(target_path)


def main() -> None:
    args = parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")

    csv_file = (args.csv_file or input_dir / "pdf_names.csv").resolve()
    if not csv_file.is_file():
        raise SystemExit(f"CSV file does not exist: {csv_file}")

    pdf_files = list(iter_pdf_files(input_dir))
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    rename_pairs = load_rename_pairs(csv_file, input_dir)
    if not rename_pairs:
        print(f"No rename instructions found in {csv_file}")
        return

    sources = {source for source, _ in rename_pairs}
    targets = [target for _, target in rename_pairs]

    duplicates = {target for target in targets if targets.count(target) > 1}
    if duplicates:
        duplicate_list = ", ".join(sorted(path.name for path in duplicates))
        raise SystemExit(f"CSV file contains duplicate target names: {duplicate_list}")

    for source_path, target_path in rename_pairs:
        if not source_path.exists():
            raise SystemExit(f"Source file does not exist: {source_path}")
        if target_path.exists() and target_path not in sources:
            raise SystemExit(f"Target file already exists: {target_path}")

    dry_run = not args.apply
    print(f"Processing {len(rename_pairs)} rename instruction(s) from {csv_file} | mode={'preview' if dry_run else 'apply'}")

    if dry_run:
        for source_path, target_path in rename_pairs:
            if source_path == target_path:
                print(f"{source_path.name} -> {target_path.name} (unchanged)")
            else:
                print(f"{source_path.name} -> {target_path.name}")
        return

    temp_paths: dict[Path, Path] = {}
    for source_path, target_path in rename_pairs:
        if source_path == target_path:
            continue
        temp_path = make_temp_path(source_path)
        while temp_path.exists() or temp_path in temp_paths.values() or temp_path in sources or temp_path in targets:
            temp_path = make_temp_path(source_path)
        source_path.rename(temp_path)
        temp_paths[source_path] = temp_path

    for source_path, target_path in rename_pairs:
        if source_path == target_path:
            print(f"{source_path.name} -> {target_path.name} (unchanged)")
            continue
        temp_paths[source_path].rename(target_path)
        print(f"{source_path.name} -> {target_path.name}")

    print(f"Done. Renamed {sum(1 for source_path, target_path in rename_pairs if source_path != target_path)} PDF(s).")


if __name__ == "__main__":
    main()