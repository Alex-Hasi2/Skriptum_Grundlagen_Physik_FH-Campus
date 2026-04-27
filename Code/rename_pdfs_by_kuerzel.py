"""Rename scanned PDF files by extracting the code above the top horizontal line on page 2."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

from pdf_workflow_core import ensure_directory, filter_pdf_files, load_truth_map, make_unique_path, sanitize_stem


DEFAULT_INPUT_DIR = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\Kurztests\Kurztest_3_v2"
)
DEFAULT_TRUTH_FILE = Path(__file__).with_name("kuerzel_ground_truth.csv")


def iter_pdf_files(input_dir: Path):
    return filter_pdf_files(input_dir)


def render_page_2(pdf_path: Path, dpi: int) -> Image.Image:
    with fitz.open(pdf_path) as document:
        if document.page_count < 2:
            raise RuntimeError("PDF has fewer than 2 pages")

        page = document[1]
        zoom = dpi / 72.0
        matrix = fitz.Matrix(zoom, zoom)
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

    return image


def crop_for_kuerzel(image: Image.Image) -> Image.Image:
    width, height = image.size
    return image.crop((0, 0, width, int(height * 0.4)))


def extract_kuerzel(text: str) -> str | None:
    patterns = [
        r"\b([A-Z0-9]{3,12})\b",
        r"\b([A-Z]{1,4}\d{1,6}[A-Z0-9]*)\b",
    ]
    cleaned = " ".join(text.split())
    for pattern in patterns:
        match = re.search(pattern, cleaned)
        if match:
            return match.group(1).upper()
    return None


def process_pdf(pdf_path: Path, output_dir: Path, dry_run: bool, rename_in_place: bool, dpi: int, truth_map: dict[str, str]) -> tuple[bool, str]:
    try:
        page_image = render_page_2(pdf_path, dpi=dpi)
    except Exception as exc:
        return False, f"{pdf_path.name}: skipped ({exc})"

    ocr_text = pytesseract.image_to_string(crop_for_kuerzel(page_image), lang="deu+eng")
    kuerzel = extract_kuerzel(ocr_text)
    expected = truth_map.get(pdf_path.stem)
    if expected:
        kuerzel = expected

    if not kuerzel:
        action = "rename" if rename_in_place else "copy"
        if dry_run:
            return False, f"{pdf_path.name}: preview {action} skipped (no kuerzel, ocr='{ocr_text.strip()}')"
        return False, f"{pdf_path.name}: skipped (no kuerzel, ocr='{ocr_text.strip()}')"

    safe_stem = sanitize_stem(kuerzel)
    target_path = make_unique_path(output_dir, safe_stem)
    action = "rename" if rename_in_place else "copy"

    if dry_run:
        if expected:
            return True, f"{pdf_path.name} -> {target_path.name} (preview {action}, truth='{expected}', ocr='{ocr_text.strip()}')"
        return True, f"{pdf_path.name} -> {target_path.name} (preview {action}, ocr='{ocr_text.strip()}')"

    if rename_in_place:
        pdf_path.rename(target_path)
    else:
        shutil.copy2(pdf_path, target_path)
    return True, f"{pdf_path.name} -> {target_path.name} ({action})"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rename scanned PDFs by OCR of the code above the top line on page 2.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/rename_pdfs_by_kuerzel.py
  python Code/rename_pdfs_by_kuerzel.py "C:/Data/PDFs" --apply
  python Code/rename_pdfs_by_kuerzel.py "C:/Data/PDFs" --output-dir "C:/Data/PDFs/renamed" --truth-file Code/kuerzel_ground_truth.csv
""",
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        metavar="INPUT_DIR",
        help=f"Folder with PDF files. Defaults to {DEFAULT_INPUT_DIR}.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        metavar="OUTPUT_DIR",
        help="Target folder for renamed/copied PDFs. If omitted, input_dir is used.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually rename files. Without this flag, the script only shows a preview.",
    )
    parser.add_argument("--dpi", type=int, default=300, help="DPI used to render page 2 for OCR.")
    parser.add_argument(
        "--truth-file",
        type=Path,
        default=DEFAULT_TRUTH_FILE,
        metavar="TRUTH_FILE",
        help="CSV file with columns source_stem,true_kuerzel. If present, these values are used as trusted overrides.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    input_dir = args.input_dir.resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"Input folder does not exist: {input_dir}")

    output_dir = ensure_directory((args.output_dir or input_dir).resolve())
    rename_in_place = output_dir == input_dir
    truth_map = load_truth_map(args.truth_file.resolve())

    pdf_files = iter_pdf_files(input_dir)
    if not pdf_files:
        print(f"No PDFs found in {input_dir}")
        return

    dry_run = not args.apply
    print(f"Processing {len(pdf_files)} PDF(s) in {input_dir} | mode={'preview' if dry_run else 'apply'}")

    success_count = 0
    for pdf_file in pdf_files:
        success, message = process_pdf(pdf_file, output_dir, dry_run, rename_in_place, args.dpi, truth_map)
        print(message)
        success_count += int(success)

    print(f"Done. Processed {success_count}/{len(pdf_files)} PDF(s).")


if __name__ == "__main__":
    main()