# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

import json
from dataclasses import asdict
from pathlib import Path

from .models import Student


def save_students(
    students: dict[str, Student],
    path: str = "school.json"
) -> None:

    data = {
        roll: asdict(student)
        for roll, student in students.items()
    }

    Path(path).write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )


def load_students(
    path: str = "school.json"
) -> dict[str, Student]:

    file_path = Path(path)

    if not file_path.exists():
        return {}

    data = json.loads(
        file_path.read_text(encoding="utf-8")
    )

    if not isinstance(data, dict):
        raise ValueError("Invalid school.json structure.")

    return {
        roll: Student(**details)
        for roll, details in data.items()
    }
