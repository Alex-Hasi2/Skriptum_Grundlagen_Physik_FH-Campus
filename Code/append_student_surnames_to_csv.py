"""Append student surnames to codes in a CSV file.

The script looks up 5-character codes in the provided student list and appends
"_<Nachname>" to the selected output column. If a code does not match exactly,
the script falls back to the closest code by character-wise similarity and prints
an informational message.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_STUDENT_LIST = Path(
    r"C:\Users\alexsc31\Documents_privat\FH Campus\Clinical_Engineering\CE28-2026\Physik\CE_28_Studierendenliste_GHKLS_SS2026.csv"
)
DEFAULT_OUTPUT_COLUMN = "new_name"
DEFAULT_SUFFIX = "_"


@dataclass(frozen=True)
class StudentEntry:
    code: str
    surname: str


@dataclass(frozen=True)
class MatchResult:
    student: StudentEntry
    score: int
    exact: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append student surnames to codes in a CSV file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python Code/append_student_surnames_to_csv.py --input-csv "C:/Data/pdf_names.csv" --code-column new_name
  python Code/append_student_surnames_to_csv.py --input-csv "C:/Data/pdf_names.csv" --code-column kuerzel --output-csv "C:/Data/pdf_names_with_names.csv"
  python Code/append_student_surnames_to_csv.py --input-csv "C:/Data/pdf_names.csv" --code-column new_name --in-place
""",
    )
    parser.add_argument(
        "--input-csv",
        required=True,
        type=Path,
        help="Input CSV file containing the code column.",
    )
    parser.add_argument(
        "--code-column",
        required=True,
        help="Name of the CSV column that contains the 5-character codes.",
    )
    parser.add_argument(
        "--output-column",
        default=DEFAULT_OUTPUT_COLUMN,
        help=f"Name of the output column to create or replace. Defaults to {DEFAULT_OUTPUT_COLUMN}.",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=None,
        help="Output CSV file. Defaults to <input-stem>_with_names.csv next to the input file.",
    )
    parser.add_argument(
        "--student-list",
        type=Path,
        default=DEFAULT_STUDENT_LIST,
        help=f"Student list CSV file. Defaults to {DEFAULT_STUDENT_LIST}.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite the input CSV instead of writing a separate output file.",
    )
    return parser.parse_args()


def normalize_surname(surname: str) -> str:
    parts = [part for part in surname.strip().split() if part]
    return "_".join(parts)


def load_student_entries(student_list: Path) -> list[StudentEntry]:
    with student_list.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        required_columns = {"Nachname", "Kürzel"}
        if not reader.fieldnames or not required_columns.issubset(set(reader.fieldnames)):
            raise SystemExit("Student list must contain the columns Nachname and Kürzel.")

        entries: list[StudentEntry] = []
        for row in reader:
            code = (row.get("Kürzel") or "").strip().upper()
            surname = normalize_surname(row.get("Nachname") or "")
            if code and surname:
                entries.append(StudentEntry(code=code, surname=surname))

    if not entries:
        raise SystemExit(f"No student entries found in {student_list}")

    return entries


def best_match(code: str, students: Iterable[StudentEntry]) -> MatchResult:
    normalized_code = code.strip().upper()
    if not normalized_code:
        raise SystemExit("Encountered an empty code value in the input CSV.")

    best_student: StudentEntry | None = None
    best_score = -1
    exact_student: StudentEntry | None = None

    for student in students:
        score = sum(1 for left, right in zip(normalized_code, student.code) if left == right)
        if student.code == normalized_code:
            exact_student = student
            best_student = student
            best_score = len(normalized_code)
            break
        if score > best_score:
            best_student = student
            best_score = score

    if best_student is None:
        raise SystemExit(f"No student entries available to match code {normalized_code}")

    return MatchResult(
        student=best_student,
        score=best_score,
        exact=exact_student is not None,
    )


def format_value(code: str, surname: str, suffix: str = DEFAULT_SUFFIX) -> str:
    return f"{code.strip().upper()}{suffix}{surname}"


def enrich_csv(
    input_csv: Path,
    output_csv: Path,
    code_column: str,
    output_column: str,
    students: list[StudentEntry],
) -> tuple[int, int]:
    matched_rows = 0
    exact_matches = 0

    with input_csv.open("r", encoding="utf-8", newline="") as input_handle:
        reader = csv.DictReader(input_handle)
        if not reader.fieldnames:
            raise SystemExit(f"Input CSV does not contain a header row: {input_csv}")
        if code_column not in reader.fieldnames:
            raise SystemExit(f"Input CSV does not contain the column {code_column}.")

        fieldnames = list(reader.fieldnames)
        if output_column not in fieldnames:
            fieldnames.append(output_column)

        with output_csv.open("w", encoding="utf-8", newline="") as output_handle:
            writer = csv.DictWriter(output_handle, fieldnames=fieldnames)
            writer.writeheader()

            for row_number, row in enumerate(reader, start=2):
                code = (row.get(code_column) or "").strip()
                if not code:
                    row[output_column] = ""
                    writer.writerow(row)
                    continue

                match = best_match(code, students)
                if not match.exact:
                    print(
                        f"INFO: row {row_number}: {code} does not match exactly; using {match.student.code} ({match.score}/5)."
                    )
                else:
                    exact_matches += 1

                row[output_column] = format_value(code, match.student.surname)
                writer.writerow(row)
                matched_rows += 1

    return matched_rows, exact_matches


def main() -> None:
    args = parse_args()

    input_csv = args.input_csv.resolve()
    if not input_csv.is_file():
        raise SystemExit(f"Input CSV does not exist: {input_csv}")

    student_list = args.student_list.resolve()
    if not student_list.is_file():
        raise SystemExit(f"Student list CSV does not exist: {student_list}")

    students = load_student_entries(student_list)
    if args.in_place:
        output_csv = input_csv
    else:
        output_csv = (args.output_csv or input_csv.with_name(f"{input_csv.stem}_with_names{input_csv.suffix}")).resolve()

    matched_rows, exact_matches = enrich_csv(
        input_csv=input_csv,
        output_csv=output_csv,
        code_column=args.code_column,
        output_column=args.output_column,
        students=students,
    )

    print(
        f"Done. Wrote {matched_rows} populated row(s) to {output_csv}. Exact matches: {exact_matches}/{matched_rows}."
    )


if __name__ == "__main__":
    main()
