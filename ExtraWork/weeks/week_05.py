## Week 5
# Task - 3, Rectangle Class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangles = [Rectangle(2, 3), Rectangle(4.5, 7.9), Rectangle(10, 1), Rectangle(5, 5)]
for i, r in enumerate(rectangles, 1):
    print(f"Rectangle {i}: area = {r.area():.2f}, perimeter = {r.perimeter():.2f}")
largest = max(rectangles, key=lambda r: r.area())
print(f"Largest area: {largest.width} x {largest.height} = {largest.area():.2f}")

# Task - 4, Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount
        print(f"Deposited £{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.balance:
            print(f"Refused: not enough money (balance £{self.balance:.2f})")
        else:
            self.balance -= amount
            print(f"Withdrew £{amount:.2f}")

    def show_balance(self):
        print(f"{self.owner}'s balance: £{self.balance:.2f}")

account = BankAccount("Tom")
account.deposit(100)
account.withdraw(30)
account.deposit(-5)
account.withdraw(500)   # should fail
account.withdraw(70)
account.show_balance()

# Task - 8, Cyber - Login Attempt Tracker
import hmac

class Account:
    MAX_ATTEMPTS = 3

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.failed_attempts = 0

    @property
    def locked(self):
        return self.failed_attempts >= self.MAX_ATTEMPTS

    def login(self, password):
        if self.locked:
            print(f"{self.username}: account locked.")
            return False
        # compare_digest avoids timing attacks
        if hmac.compare_digest(password.encode(), self.password.encode()):
            self.failed_attempts = 0
            return True
        self.failed_attempts += 1
        return False

acc = Account("alice", "S3cret!")
print(acc.login("wrong"))     # False
print(acc.login("S3cret!"))   # True, resets the counter
for _ in range(3):
    print(acc.login("guess")) # False x3 -> locked
print(acc.login("S3cret!"))   # False, locked even with the right password
print("Locked:", acc.locked)

# Task - 9, Gradebook
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_mark(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.average()
        return None

    def top_student(self):
        return max(self.students, key=lambda s: s.average()) if self.students else None

course = Course("Cyber Security")
for name, marks in [("Alice", [78, 85, 90]), ("Bob", [60, 72, 65]),
                    ("Charlie", [88, 92, 95]), ("Diana", [70, 68, 75])]:
    course.add_student(Student(name, marks))
for student in course.students:
    print(f"{student.name}: {course.average_mark(student.name):.2f}")
top = course.top_student()
print(f"Top student: {top.name} ({top.average():.2f})")

