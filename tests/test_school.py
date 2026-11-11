
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

from school.models import Student
from school.grades import average
from school.service import report_card, class_ranking
from school.storage import save_students, load_students


def test_new_student_has_empty_marks() -> None:
    student = Student("Ali", "12")
    assert student.marks == []


def test_students_do_not_share_marks_lists() -> None:
    first = Student("Ali", "12")
    second = Student("Sara", "13")

    first.marks.append(80)

    assert second.marks == []


def test_average() -> None:
    assert average([80, 90, 100]) == 90


def test_report_card_grade() -> None:
    student = Student("Sara", "13", [90, 80])
    result = report_card(student)

    assert "Average: 85.00" in result
    assert "Grade: A" in result


def test_empty_report() -> None:
    student = Student("Ali", "12")

    assert "No marks recorded yet" in report_card(student)


def test_class_ranking() -> None:
    students = {
        "12": Student("Ali", "12", [60, 70]),
        "13": Student("Sara", "13", [90, 95]),
    }

    ranked = class_ranking(students)

    assert [student.name for student in ranked] == [
        "Sara", "Ali"
    ]


def test_save_and_load(tmp_path) -> None:
    path = str(tmp_path / "school.json")

    original = {
        "12": Student("Ali", "12", [85, 90])
    }

    save_students(original, path)
    loaded = load_students(path)

    assert loaded["12"] == original["12"]


def test_load_missing_file(tmp_path) -> None:
    path = str(tmp_path / "missing.json")

    assert load_students(path) == {}
