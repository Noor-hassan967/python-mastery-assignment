# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

import math


def grade(mark: float) -> str:
    if not math.isfinite(mark) or not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 33:
        return "D"
    return "Fail"


def average(marks: list[float]) -> float:
    if not marks:
        raise ValueError("Cannot average an empty marks list.")

    return sum(marks) / len(marks)
