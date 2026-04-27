"""Merge all PDF files in a folder into one PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

from pdf_workflow_core import filter_pdf_files, load_pdf_classes, resolve_output_dir


DEFAULT_INPUT_DIR = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\Kurztests\Kurztest_3_v2"
)


def merge_pdf_files(input_dir: Path, output_path: Path, pdf_reader_cls: type, pdf_writer_cls: type) -> int:
    writer = pdf_writer_cls()
    pdf_files = filter_pdf_files(input_dir, excluded_paths=[output_path])

    total_pages = 0
    for pdf_path in pdf_files:
        reader = pdf_reader_cls(str(pdf_path))
        if getattr(reader, "is_encrypted", False):
            try:
                reader.decrypt("")
            except Exception as exc:  # pragma: no cover - depends on source PDFs
                raise RuntimeError(f"Cannot read encrypted PDF: {pdf_path}") from exc

        for page in reader.pages:
            writer.add_page(page)
            total_pages += 1

    with output_path.open("wb") as output_handle:
        writer.write(output_handle)

    return total_pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge every PDF in a folder into one PDF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/merge_pdfs.py
  python Code/merge_pdfs.py "C:/Data/PDFs"
  python Code/merge_pdfs.py "C:/Data/PDFs" --output-name combined.pdf --output-dir "C:/Data/PDFs/merged"
""",
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        metavar="INPUT_DIR",
        help=f"Folder containing the PDF files to merge. Defaults to {DEFAULT_INPUT_DIR}.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        metavar="OUTPUT_DIR",
        help="Folder where the merged PDF should be written. Defaults to a 'merged_pdf' folder inside the input directory.",
    )
    parser.add_argument(
        "--output-name",
        type=str,
        default="merged.pdf",
        metavar="OUTPUT_NAME",
        help="Filename of the merged PDF inside the output directory. Defaults to merged.pdf.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")

    pdf_reader_cls, pdf_writer_cls, library_name = load_pdf_classes()
    output_dir = resolve_output_dir(input_dir, args.output_dir, "merged_pdf")
    output_path = output_dir / args.output_name

    pdf_files = filter_pdf_files(input_dir, excluded_paths=[output_path])
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    print(f"Using {library_name} to merge {len(pdf_files)} PDF file(s).")
    total_pages = merge_pdf_files(input_dir, output_path, pdf_reader_cls, pdf_writer_cls)
    print(f"Done. Created {output_path} with {total_pages} pages.")


if __name__ == "__main__":
    main()