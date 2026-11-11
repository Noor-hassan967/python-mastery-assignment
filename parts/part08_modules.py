# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 8 - MODULES AND PACKAGES

import math
import random
import statistics
from datetime import date

from school_tools import (
    area_of_circle,
    is_even,
    greet,
    average,
    grade,
    report
)

# Warm-up: Standard Library Tour
print("=== STANDARD LIBRARY ===")

print("Square root of 144:", math.sqrt(144))

students = ["Ali", "Sara", "Hamza", "Ayesha"]
print("Random student:", random.choice(students))

today = date.today()
december_31 = date(today.year, 12, 31)
days_left = (december_31 - today).days
print("Days until December 31:", days_left)

marks = [70, 85, 90, 65, 80]
print("Mean:", statistics.mean(marks))
print("Median:", statistics.median(marks))


# Build: Importing Our Own Module
print("\n=== CUSTOM SCHOOL MODULE ===")

print("Area of circle:", round(area_of_circle(5), 2))
print("Is 12 even?", is_even(12))
print(greet("Ahmed", "ur"))

print("Average:", average([80, 90, 70]))
print("Grade:", grade(85))
print(report("Sara", [95, 85, 90]))

# school_tools.py contains a __main__ test.
# Its test block does not run when the module is imported.
