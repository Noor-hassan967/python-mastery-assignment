# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 12 - DEBUGGING AND TESTING

# Warm-up: Fix Three Bugs

marks = [90, 25, 70]
passing = []

# Fix 1: Iterate over every mark.
# Original code skipped the last item.
for mark in marks:

    # Fix 2: Append instead of replacing the list.
    if mark >= 33:
        passing.append(mark)

# Fix 3: Divide by the number of passing marks,
# not the number of all marks.
if passing:
    avg = sum(passing) / len(passing)
    print("Passing marks:", passing)
    print("Average:", avg)
else:
    print("No passing marks found.")

# Expected average: 80.0

# Build:
# Automated grade tests are implemented
# in tests/test_grades.py using pytest.
