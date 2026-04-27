"""Export PDF filenames from a folder into a CSV file.

The CSV contains a first column with the current file name and a second empty
column that can later be filled with the desired target file name.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from pdf_workflow_core import ensure_directory, iter_pdf_files


DEFAULT_INPUT_DIR = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\Kurztests\Kurztest_3_v2"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write all PDF filenames from a folder into a CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/export_pdf_names_to_csv.py
  python Code/export_pdf_names_to_csv.py "C:/Data/PDFs"
  python Code/export_pdf_names_to_csv.py "C:/Data/PDFs" --csv-file "C:/Data/PDFs/pdf_names.csv"
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
        help="CSV file to write. Defaults to a pdf_names.csv file inside the input directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")

    csv_file = (args.csv_file or input_dir / "pdf_names.csv").resolve()
    ensure_directory(csv_file.parent)

    pdf_files = list(iter_pdf_files(input_dir))
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    with csv_file.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["current_name", "new_name"])
        for pdf_file in pdf_files:
            writer.writerow([pdf_file.name, ""])

    print(f"Wrote {len(pdf_files)} PDF name(s) to {csv_file}")


if __name__ == "__main__":
    main()