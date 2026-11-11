# Python Mastery Assignment

## Project Overview

This repository contains my Python Mastery Assignment, covering 12 practical programming topics and a final project called **School Manager**.

The assignment demonstrates Python fundamentals, object-oriented programming, file handling, modular programming, error handling, and automated testing.

## Assignment Parts

| Part | Topic |
|---|---|
| 01 | Variables, Data Types, Input and Output |
| 02 | Conditional Statements |
| 03 | Loops |
| 04 | Lists, Dictionaries, Tuples and Sets |
| 05 | Functions and Comprehensions |
| 06 | References and Mutability |
| 07 | Exception Handling and File Operations |
| 08 | Modules and Packages |
| 09 | Object-Oriented Programming |
| 10 | Iterators and Generators |
| 11 | Type Hints and Dataclasses |
| 12 | Debugging and Automated Testing |

The individual part files contain the core practical exercises.

## Final Project — School Manager

School Manager is a menu-driven Python application for managing student information and academic results.

### Features

- Add students using names and roll numbers.
- Record student marks.
- Generate report cards showing averages and grades.
- Rank students according to their average marks.
- Save and load student records using JSON.
- Handle invalid menu selections and marks.
- Organize application code into reusable Python modules.
- Verify core functionality using automated pytest tests.

### Technologies Used

- Python 3
- Python Standard Library
- Dataclasses and Type Hints
- JSON for Data Persistence
- Pytest for Automated Testing
- Git and GitHub for Version Control

## How to Run the Project

1. Clone or download the repository.
2. Open a terminal in the project folder.
3. Create a virtual environment using `python3 -m venv .venv` and activate it with `source .venv/bin/activate`.
4. Install dependencies using `python -m pip install -r requirements.txt`.
5. Run the application using `python main.py` and execute the tests using `python -m pytest -v`.

## Running Individual Assignment Parts

Each exercise is stored in the `parts/` directory.

For example:

```bash
python parts/part01_variables.py
python parts/part02_conditions.py
python parts/part03_loops.py
```

Other parts can be executed using their corresponding filenames.

## Automated Testing

The project includes pytest tests for grading, student records, rankings, report cards, and JSON persistence.

**Latest verified local test result: 21 tests passed.**

Run the tests using:

```bash
python -m pytest -v
```

The tests are stored in the `tests/` directory.

## Project Structure

```text
python-mastery-assignment/
├── parts/              # Python assignment exercises
├── school/             # School Manager modules
├── tests/              # Automated pytest tests
├── main.py             # School Manager entry point
├── requirements.txt    # Development dependencies
├── .gitignore          # Excluded local files
└── README.md           # Project documentation
```

## Notes

- Student records are saved locally in `school.json`.
- The virtual environment and generated data files are excluded from Git.
- The repository focuses on the required core exercises and School Manager features.
- Optional individual challenge tasks and the optional AI integration are not included.

## Assignment Information

**Course:** Python Programming  
**Assignment:** Python Mastery Assignment — Build Real Things  
**Final Project:** School Manager  
**Submission:** GitHub Repository
