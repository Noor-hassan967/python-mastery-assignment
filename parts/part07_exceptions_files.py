# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 7 - EXCEPTIONS AND FILE HANDLING

from datetime import date
from pathlib import Path

# Warm-up: Safe Division
print("=== SAFE DIVISION ===")

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result:.2f}")
        break

    except ValueError:
        print("Invalid input. Please enter numbers.")

    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")


# Build: Daily Diary
diary_file = Path("diary.txt")

while True:
    print("\n=== DAILY DIARY ===")
    print("1. Write Entry")
    print("2. Read Entries")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Write today's note: ")
        today = date.today()

        with diary_file.open("a", encoding="utf-8") as file:
            file.write(f"{today}: {note}\n")

        print("Diary entry saved.")

    elif choice == "2":
        if diary_file.exists():
            print("\n=== PREVIOUS ENTRIES ===")
            with diary_file.open("r", encoding="utf-8") as file:
                print(file.read())
        else:
            print("No entries yet.")

    elif choice == "3":
        print("Diary closed.")
        break

    else:
        print("Invalid choice.")
