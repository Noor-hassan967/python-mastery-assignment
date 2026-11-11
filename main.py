# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026


# FINAL PROJECT - SCHOOL MANAGER

import logging

from school.models import Student
from school.grades import grade, average
from school.service import report_card, class_ranking
from school.storage import load_students, save_students

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)


def add_student(students: dict[str, Student]) -> None:
    name = input("Student name: ").strip()
    roll = input("Roll number: ").strip()

    if not name or not roll:
        print("Name and roll number cannot be blank.")

    elif roll in students:
        print("That roll number already exists.")

    else:
        students[roll] = Student(
            name=name,
            roll_number=roll
        )
        print("Student added.")


def add_marks(students: dict[str, Student]) -> None:
    roll = input("Roll number: ").strip()
    student = students.get(roll)

    if student is None:
        print("Student not found.")
        return

    try:
        mark = float(input("Enter mark (0-100): "))
        grade(mark)  # Validate before saving.

    except ValueError:
        print("Invalid mark. Enter a number from 0 to 100.")
        return

    student.marks.append(mark)
    print("Mark added.")


def show_report(students: dict[str, Student]) -> None:
    roll = input("Roll number: ").strip()
    student = students.get(roll)

    if student is None:
        print("Student not found.")

    else:
        print("\n===== REPORT CARD =====")
        print(report_card(student))


def show_ranking(students: dict[str, Student]) -> None:
    ranked = class_ranking(students)

    if not ranked:
        print("No students with marks yet.")
        return

    print("\n===== CLASS RANKING =====")

    for position, student in enumerate(ranked, start=1):
        avg = average(student.marks)

        print(
            f"{position}. {student.name} "
            f"(Roll {student.roll_number}) "
            f"- Average: {avg:.2f}"
        )


def main() -> None:
    try:
        students = load_students()

    except (OSError, ValueError, TypeError, KeyError) as error:
        logging.error("Could not load school.json: %s", error)
        print("Please fix the data file before starting again.")
        return

    while True:
        print("\n===== SCHOOL MANAGER =====")
        print("1. Add student")
        print("2. Add marks")
        print("3. Show report card")
        print("4. Class ranking")
        print("5. Save and exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            add_marks(students)

        elif choice == "3":
            show_report(students)

        elif choice == "4":
            show_ranking(students)

        elif choice == "5":
            try:
                save_students(students)
                print("Data saved. Goodbye!")
                return

            except OSError as error:
                logging.error("Save failed: %s", error)
                print("Could not save. Session remains open.")

        else:
            print("Invalid menu choice. Enter 1-5.")


if __name__ == "__main__":
    main()
