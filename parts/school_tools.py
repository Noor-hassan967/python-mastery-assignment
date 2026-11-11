
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# SCHOOL TOOLS - REUSABLE FUNCTIONS

import math


def area_of_circle(radius: float) -> float:
    return math.pi * radius ** 2


def is_even(number: int) -> bool:
    return number % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"


def average(marks: list[float]) -> float:
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    return sum(marks) / len(marks)


def grade(avg: float) -> str:
    if avg < 0 or avg > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"


def report(name: str, marks: list[float]) -> str:
    avg = average(marks)
    return f"{name}: Average {avg:.2f}, Grade {grade(avg)}"


if __name__ == "__main__":
    print("Running school_tools directly")
    print(greet("Ali"))
    print(report("Sara", [80, 90, 85]))
