# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 2 - CONDITIONS

# Warm-up: Even/Odd and Positive/Negative
number = int(input("Enter an integer: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Build: Grade Calculator
print("\n=== GRADE CALCULATOR ===")
marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: Fail")
