
# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

import pytest

from school.grades import grade


@pytest.mark.parametrize(
    "mark, expected",
    [
        (0, "Fail"),
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A"),
        (100, "A"),
    ],
)
def test_grade_boundaries(
    mark: float,
    expected: str
) -> None:
    assert grade(mark) == expected


@pytest.mark.parametrize(
    "mark",
    [-1, 101, float("nan")]
)
def test_invalid_marks(mark: float) -> None:
    with pytest.raises(ValueError):
        grade(mark)
