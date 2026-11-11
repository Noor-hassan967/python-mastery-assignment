# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    roll_number: str
    marks: list[float] = field(default_factory=list)
