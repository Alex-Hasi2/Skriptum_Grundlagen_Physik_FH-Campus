"""Shared helpers for PDF workflows.

The module keeps common filesystem and PDF-loading logic in one place so the
split, merge, and rename scripts can stay small and focused.
"""

from __future__ import annotations

import csv
from importlib import import_module
from pathlib import Path
from typing import Iterable, Iterator, Sequence, Tuple


def load_pdf_classes() -> Tuple[type, type, str]:
    """Return PdfReader and PdfWriter from pypdf or PyPDF2."""

    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = import_module(module_name)
        except ImportError:
            continue

        pdf_reader = getattr(module, "PdfReader", None)
        pdf_writer = getattr(module, "PdfWriter", None)
        if pdf_reader is not None and pdf_writer is not None:
            return pdf_reader, pdf_writer, module_name

    raise SystemExit(
        "This script requires either 'pypdf' or 'PyPDF2'. Install one of them with 'pip install pypdf'."
    )


def iter_pdf_files(input_dir: Path) -> Iterator[Path]:
    """Yield PDF files in deterministic order."""

    for path in sorted(input_dir.iterdir()):
        if path.is_file() and path.suffix.lower() == ".pdf":
            yield path


def ensure_directory(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def make_unique_path(base_dir: Path, stem: str, suffix: str = ".pdf") -> Path:
    """Return a unique path inside base_dir for the given stem."""

    candidate = base_dir / f"{stem}{suffix}"
    if not candidate.exists():
        return candidate

    index = 1
    while True:
        candidate = base_dir / f"{stem}_{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def load_truth_map(csv_path: Path) -> dict[str, str]:
    """Load a CSV mapping of source_stem -> true_kuerzel."""

    if not csv_path.exists():
        return {}

    mapping: dict[str, str] = {}
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            source_stem = (row.get("source_stem") or "").strip()
            true_kuerzel = (row.get("true_kuerzel") or "").strip().upper()
            if source_stem and true_kuerzel:
                mapping[source_stem] = true_kuerzel
    return mapping


def should_skip_path(path: Path, excluded_paths: Iterable[Path]) -> bool:
    excluded = {item.resolve() for item in excluded_paths}
    return path.resolve() in excluded


def filter_pdf_files(input_dir: Path, excluded_paths: Iterable[Path] | None = None) -> list[Path]:
    excluded_paths = excluded_paths or []
    return [path for path in iter_pdf_files(input_dir) if not should_skip_path(path, excluded_paths)]


def sanitize_stem(stem: str) -> str:
    """Convert a free-form stem into a safe PDF filename stem."""

    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in stem).strip("_") or "output"


def resolve_output_dir(input_dir: Path, output_dir: Path | None, default_name: str) -> Path:
    """Resolve an output directory, falling back to a folder inside input_dir."""

    return ensure_directory((output_dir or input_dir / default_name).resolve())


def chunk_ranges(page_count: int, pages_per_file: int) -> Iterator[tuple[int, int]]:
    for start_page in range(0, page_count, pages_per_file):
        yield start_page, min(start_page + pages_per_file, page_count)


def excluded_output_paths(output_dir: Path, output_names: Sequence[str]) -> list[Path]:
    return [output_dir / output_name for output_name in output_names]