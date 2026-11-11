# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 10 - ITERATORS AND GENERATORS

from pathlib import Path


# Warm-up: Countdown Generator
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


def evens(limit):
    for number in range(0, limit + 1, 2):
        yield number


print("=== COUNTDOWN ===")
for value in countdown(5):
    print(value)

print("Even numbers:", list(evens(10)))


# Build: Big File Reader
log_file = Path("sample_log.txt")

# Generate a sample file with 50 lines.
with log_file.open("w", encoding="utf-8") as file:
    for number in range(1, 51):
        if number % 7 == 0:
            file.write(f"Line {number}: ERROR - Failed request\n")
        else:
            file.write(f"Line {number}: INFO - Success\n")


def read_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line


print("\n=== LOG FILE ANALYSIS ===")

error_count = 0

for error_line in only_errors(read_lines(log_file)):
    print(error_line.strip())
    error_count += 1

print("Total errors:", error_count)
