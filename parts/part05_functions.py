
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 5 - FUNCTIONS AND COMPREHENSIONS

import math


# Warm-up: Helper Functions
def area_of_circle(radius: float) -> float:
    return math.pi * radius ** 2


def is_even(number: int) -> bool:
    return number % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"


print("=== HELPER FUNCTIONS ===")

for radius in [2, 5, 10]:
    print(f"Radius {radius}: Area = {area_of_circle(radius):.2f}")

for number in [4, 7, 12]:
    print(f"{number} is even: {is_even(number)}")

print(greet("Ali"))
print(greet("Sara", "ur"))
print(greet("Hamza", "en"))


# Build: Marks Toolkit
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
    result = grade(avg)
    return f"{name}: Average = {avg:.2f}, Grade = {result}"


print("\n=== MARKS TOOLKIT ===")
print(report("Ali", [80, 75, 90]))
print(report("Sara", [95, 92, 88]))
print(report("Hamza", [45, 52, 60]))
