# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026


from .models import Student
from .grades import grade, average


def report_card(student: Student) -> str:
    if not student.marks:
        return (
            f"{student.name} (Roll {student.roll_number}): "
            "No marks recorded yet."
        )

    avg = average(student.marks)

    return (
        f"Name: {student.name}\n"
        f"Roll Number: {student.roll_number}\n"
        f"Marks: {student.marks}\n"
        f"Average: {avg:.2f}\n"
        f"Grade: {grade(avg)}"
    )


def class_ranking(
    students: dict[str, Student]
) -> list[Student]:

    with_marks = [
        student
        for student in students.values()
        if student.marks
    ]

    return sorted(
        with_marks,
        key=lambda student: average(student.marks),
        reverse=True
    )
