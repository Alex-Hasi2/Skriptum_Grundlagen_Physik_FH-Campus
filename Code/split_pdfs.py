"""Split all PDF files in a folder into smaller PDFs with a fixed page count."""

from __future__ import annotations

import argparse
from pathlib import Path

from pdf_workflow_core import chunk_ranges, filter_pdf_files, load_pdf_classes, resolve_output_dir


DEFAULT_INPUT_DIR = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\Kurztests\Kurztest_3_v2"
)


def split_pdf_file(pdf_path: Path, output_dir: Path, pages_per_file: int, pdf_reader_cls: type, pdf_writer_cls: type) -> int:
    reader = pdf_reader_cls(str(pdf_path))
    if getattr(reader, "is_encrypted", False):
        try:
            reader.decrypt("")
        except Exception as exc:  # pragma: no cover - depends on source PDFs
            raise RuntimeError(f"Cannot read encrypted PDF: {pdf_path}") from exc

    page_count = len(reader.pages)
    if page_count == 0:
        print(f"Skipping empty PDF: {pdf_path.name}")
        return 0

    total_chunks = (page_count + pages_per_file - 1) // pages_per_file
    chunk_count = 0

    for start_page, end_page in chunk_ranges(page_count, pages_per_file):
        writer = pdf_writer_cls()
        for page_index in range(start_page, end_page):
            writer.add_page(reader.pages[page_index])

        chunk_count += 1
        output_path = output_dir / f"{pdf_path.stem}_{chunk_count:03d}of{total_chunks:03d}.pdf"
        with output_path.open("wb") as output_handle:
            writer.write(output_handle)

    print(f"{pdf_path.name}: {page_count} pages -> {chunk_count} files")
    return chunk_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split every PDF in a folder into smaller PDFs with a fixed page count.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/split_pdfs.py
  python Code/split_pdfs.py "C:/Data/PDFs"
  python Code/split_pdfs.py "C:/Data/PDFs" --pages-per-file 4 --output-dir "C:/Data/PDFs/split_out"
""",
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        metavar="INPUT_DIR",
        help=f"Folder containing the PDF files to split. Defaults to {DEFAULT_INPUT_DIR}.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        metavar="OUTPUT_DIR",
        help="Folder where the split PDFs should be written. Defaults to a 'split_2_pages' folder inside the input directory.",
    )
    parser.add_argument("--pages-per-file", type=int, default=2, metavar="N", help="Number of pages per output PDF. Defaults to 2.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")
    if args.pages_per_file < 1:
        raise SystemExit("--pages-per-file must be at least 1.")

    pdf_reader_cls, pdf_writer_cls, library_name = load_pdf_classes()
    output_dir = resolve_output_dir(input_dir, args.output_dir, f"split_{args.pages_per_file}_pages")

    pdf_files = filter_pdf_files(input_dir)
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    print(f"Using {library_name} to split {len(pdf_files)} PDF file(s).")

    total_chunks = 0
    for pdf_file in pdf_files:
        total_chunks += split_pdf_file(pdf_file, output_dir, args.pages_per_file, pdf_reader_cls, pdf_writer_cls)

    print(f"Done. Created {total_chunks} output PDF(s) in {output_dir}.")


if __name__ == "__main__":
    main()