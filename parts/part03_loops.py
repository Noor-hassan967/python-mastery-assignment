
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026


# PART 3 - LOOPS

# Warm-up: Multiplication Table
number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Build: ATM PIN Checker
print("\n=== ATM PIN CHECKER ===")

correct_pin = "4321"
max_attempts = 3

for attempt in range(max_attempts):
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("Welcome!")
        break

    remaining = max_attempts - attempt - 1
    print(f"Incorrect PIN. Attempts left: {remaining}")

else:
    print("Card blocked")
