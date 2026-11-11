# Name: Muhammad Noor Hassan
# Roll Number: TRN-2026-000808
# Date: 11 November 2026

# PART 9 - OBJECT-ORIENTED PROGRAMMING

# Warm-up: Student Class
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def __str__(self):
        return (
            f"{self.name} (Roll {self.roll_number}): "
            f"avg {self.average():.1f}"
        )


student = Student("Ali", 12)
student.add_mark(80)
student.add_mark(90)
student.add_mark(73)

print("=== STUDENT ===")
print(student)


# Build: Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Starting balance cannot be negative.")

        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")

        self.balance += amount
        self.history.append(f"Deposited Rs {amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")

        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        self.history.append(f"Withdrew Rs {amount:.2f}")

    def show_history(self):
        print(f"\nTransaction History for {self.owner}")

        for transaction in self.history:
            print(transaction)

        print(f"Current Balance: Rs {self.balance:.2f}")


account = BankAccount("Ahmed", 1000)

try:
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(2000)

except ValueError as error:
    print("Transaction rejected:", error)

account.show_history()
