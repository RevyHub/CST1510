# Legacy combined copy. Run the separate files in weeks/ instead.
# Running this file executes every week's exercises in sequence.

## Week 1
# Task - 1, Questionaire
Name = input("Enter your name: ")
Interest = input("Enter your interest: ")
Nationality = input("Enter your nationality: ")
Course = input("Enter your course: ")
Experience = input("Enter your programming experience: ")
print("User Information:")
print(f"\tName: {Name}")
print(f"\tInterest: {Interest}")
print(f"\tNationality: {Nationality}")
print(f"\tCourse: {Course}")
print(f"\tExperience: {Experience}")

# Task - 2, Rectangle Area and Perimiter
width = 4.5
height = 7.9
area = width * height
perimiter = 2 * (width + height)
print(f"The Area is {area}")
print(f"The Perimiter is {perimiter}")

# Task - 3, Convert Pounds to Kilograms
ask = input("Please enter a number: ")
pounds = float(ask)
kg = pounds * 0.454
print(f"{pounds} lb = {kg:.2f} kg")

# Task - 4, Convert Feet into Meters
ask = input("Please enter a number: ")
foot = float(ask)
meters = foot * 0.305
print(f"{foot} ft = {meters:.2f} meters")

# Task - 5, Quick Check
# 1. input() always returns a string (str), even if the user types a number.
# float() and int() convert that string to a decimal or whole number.
print(type(input("x")))  # <class 'str'>
# 2. An escape sequence is a backslash followed by a character that represents
# a special character inside a string.
print("Hello\nWorld")  # \n = new line
# \t = tab, \\ = literal backslash, \" = literal quote
# 3. / is true division and always returns a float.
# // is floor division and rounds down to the nearest whole number.
print(7 / 2)   # 3.5
print(7 // 2)  # 3

# Task - 6, Total time to watch a series
# EPS = Episodes Per Season
# S1S = Season 1 Seconds
# OS = Other Seconds
# TS = Total Seconds
EPS = 10
S1S = 45 * 60 + 35
OS = 35 * 60 + 15
TS = EPS * S1S
TS += 4 * EPS * OS
hours = TS // 3600
minutes = (TS % 3600) // 60
seconds = TS % 60
print(f"Total time: {hours}h {minutes}m {seconds}s")

# Task - 7, Savings Projections - 3 years
# WPY - Weeks Per Year
WPY = 52
years = 3
total_weeks = WPY * years
savings = 0
savings += 10 * total_weeks # £10 every week for 3 years
savings += 20 * WPY # Year 1 bonus: +£20 each week
savings -= 0.50 * (total_weeks // 2) # -£0.50 every 2 weeks (sister)
print(f"Final savings after 3 years: £{savings:.2f}")

# Task - 8, Cyber HTTP Log Composer
ip = input("Enter IP address: ")
method = input("Enter HTTP method: ")
path = input("Enter path: ")
status = input("Enter status code: ")
size = input("Enter bytes: ")
print(f'{ip} - "{method} {path}" {status} {size}')

# Task - 9, Pure Python EDA - Data Metadata
name = input("Enter dataset name: ")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
print(f'"{name}"')
print(f"Rows: {rows}")
print(f"Columns: {columns}")
print(f"Cells: {rows * columns}")

# Task - 10, IT - INI-style Config file printer
"""Theres two ways in doing this but I found it works better when you do this way"""
pair1 = input("Enter first key=value: ")
pair2 = input("Enter second key=value: ")
pair3 = input("Enter third key=value: ")
print("[config]")
for pair in (pair1, pair2, pair3):
    if "=" in pair:
        key, value = pair.split("=", 1)
        print(f"\t{key.strip()} = {value.strip()}")
    else:
        print(f"\t# invalid entry: {pair}")

# Task - 11, Sum of First N Integers
n = int(input("Enter a positive integer n: "))
total = n * (n + 1) // 2
print(f"Sum of 1{n} = {total}")

# Task - 12, Population Projection - 5 years
# SPY = Seconds Per Year
# NC = Net Change
population = 312032486
SPY = 365 * 24 * 60 * 60
births = SPY // 7
deaths = SPY // 13
immigrants = SPY // 45
NC = births - deaths + immigrants
for year in range(1, 6):
    population += NC
    print(f"Year {year}: {population:,}")

# Task - 13, Payroll Statement
# FR = Federal Rate
# SR = State Rate
name = input("Enter employee name: ")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
FR = float(input("Enter federal tax rate (%): ")) / 100
SR = float(input("Enter state tax rate (%): ")) / 100
gross = hours * rate
federal = gross * FR
state = gross * SR
net = gross - federal - state
print(f"Employee: {name}")
print(f"Gross pay: £{gross:.2f}")
print(f"Federal withholding: £{federal:.2f}")
print(f"State withholding: £{state:.2f}")
print(f"Net pay: £{net:.2f}")

## Week 2
# Task - 1, Password Strength Checker
password = input("Enter a password: ")
if len(password) >= 12:
    print("Strong")
elif len(password) >= 8:
    print("Moderate")
else:
    print("Weak")

# Task - 2, Multiplacation Quiz
from random import randint
num1 = randint(0, 9)
num2 = randint(0, 9)
answer = int(input(f"What is {num1} * {num2}? "))
if answer == num1 * num2:
    print("True - correct!")
else:
    print(f"False - the correct answer is {num1 * num2}")

# Task - 3, Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Task - 4, Body Mass Index Calculator
# Wlb = Weight in pounds
# HIn = Height in Inches
# WKG = Weight in Kilograms
# HM = Height in Meters
Wlb = float(input("Enter your weight (lbs): "))
HIn = float(input("Enter ypur height (Inches): "))
WKG = Wlb * 0.45359237
HM = HIn * 0.0254
bmi = WKG / (HM ** 2)
print(f"BMI: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")

# Task - 5, Negative Numbers
"""For this one I took the liberty in adding a time lib so you can see it print
   Because for me it did not print slowly"""
import time
for i in range(-10, 0):
    print(i)
    time.sleep(0.2)

# Task - 6, Number Patterns
"""Likewise for this one ill be using the time import for slower displays"""
import time
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
        time.sleep(0.2)
    print()

# Task - 7, Sum of Numbers from 1 to n
n = int(input("Enter the value n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum of all numbers until {n} is {total}")

# Task - 8, Multiplaction Table of a Number
num = int(input("Enter a number: "))
for i in range(10):
    print(f"{i} x {num} = {i * num}")

# Task - 9, Multiplacation Table Grid
for i in range(10):
    for j in range(10):
        print(f"{i * j:3}", end=" ")
    print()

# Task - 10, Dog Years
# HY = Human Years
HY = float(input("Enter human years: "))
if HY < 0:
    print("Error: age cannot be negative.")
elif HY <= 2:
    print(f"Dog years: {HY * 10.5}")
else:
    print(f"Dog years: {2 * 10.5 + (HY - 2) * 4}")

# Task - 11, Vowel or Consonant
letter = input("Enter a letter: ").lower()
if letter in ("a", "e", "i", "o", "u"):
    print("That letter is a vowel.")
elif letter == "y":
    print("Sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print("That letter is a consonant.")

# Task - 12, Reverse Number Pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Task - 13, Find the Highest Sore
# TN = Top Name
# TS = Top Score
count = int(input("Enter the number of students: "))
TN = ""
TS = float("-inf")
for _ in range(count):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    if score > TS:
        TS = score
        TN = name
print(f"Highest score: {TN} with {TS}")

# Task - 14, Guessing Game
from random import randint
secret = randint(1, 100)
tries = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    tries += 1
    if guess > secret:
        print("Too large")
    elif guess < secret:
        print("Too small")
    else:
        print(f"Correct! You needed {tries} tries.")
        break

# Task - 15, Lottery - Two Digit
from random import randint
lottery = str(randint(10, 99))
guess = input("Enter a two-digit number: ")
print(f"Lottery number: {lottery}")
if guess == lottery:
    print("Exact match: you win £10,000")
elif sorted(guess) == sorted(lottery):
    print("All digits match: you win £3,000")
elif any(d in lottery for d in guess):
    print("One digit matches: you win £1,000")
else:
    print("Sorry, no match")

# Task - 16, Lottery - Three Digit
from random import randint
lottery = str(randint(100, 999))
guess = input("Enter a three-digit number: ")
print(f"Lottery number: {lottery}")
if guess == lottery:
    print("Exact match: you win £10,000")
elif sorted(guess) == sorted(lottery):
    print("All digits match: you win £3,000")
elif any(d in lottery for d in guess):
    print("One digit matches: you win £1,000")
else:
    print("Sorry, no match")

# Task - 17, Find the TWO high scores
count = int(input("Enter the number of students: "))
highest = float("-inf")
second = float("-inf")
for _ in range(count):
    score = float(input("Enter student score: "))
    if score > highest:
        second = highest
        highest = score
    elif score > second:
        second = score
print(f"Highest score: {highest}")
print(f"Second highest score: {second}")

# Task - 18, Password Cracker
actual = "MDX123"
guess = input("Enter your password guess: ")
"""This is a case sensitive, position by position comparison"""
matches = 0
for i in range(min(len(actual), len(guess))):
    if guess[i] == actual[i]:
        matches += 1
accuracy = matches / len(actual) * 100
if guess == actual:
    print("Password cracked!")
else:
    print(f"Accuracy: {accuracy:.0f}%")

## Week 3
# Task - 1, Quiz
from random import randint

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def exponent(a, b): return a ** b

def divide(a, b):
    return a / b if b != 0 else None

def remainder(a, b):
    return a % b if b != 0 else None

OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
    "5": ("**", exponent),
    "6": ("%", remainder),
}

def quiz():
    score = 0
    asked = 0
    while True:
        print("\n1) Add  2) Subtract  3) Multiply  4) Divide  5) Exponent  6) Remainder  q) Quit")
        choice = input("Choose an operation: ").lower()
        if choice == "q":
            break
        if choice not in OPERATIONS:
            print("Invalid choice.")
            continue
        symbol, func = OPERATIONS[choice]
        a, b = randint(0, 9), randint(0, 9)
        correct = func(a, b)
        if correct is None:
            print(f"Error: {a} {symbol} {b} divides by zero. Generating a new question.")
            continue
        try:
            answer = float(input(f"What is {a} {symbol} {b}? "))
        except ValueError:
            print("Please enter a number.")
            continue
        asked += 1
        if abs(answer - correct) < 0.01:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong - the answer is {correct:.2f}")
    print(f"Final score: {score}/{asked}")

quiz()

# Task - 2, Scientific Calculator (Unit Conversion Chart)
# Each function converts first unit -> second unit when fwd=True, and back when fwd=False
def metres_feet(v, fwd=True): return v * 3.28084 if fwd else v / 3.28084
def inches_cm(v, fwd=True): return v * 2.54 if fwd else v / 2.54
def miles_km(v, fwd=True): return v * 1.60934 if fwd else v / 1.60934
def celsius_fahrenheit(v, fwd=True): return v * 9 / 5 + 32 if fwd else (v - 32) * 5 / 9
def celsius_kelvin(v, fwd=True): return v + 273.15 if fwd else v - 273.15
def kg_pounds(v, fwd=True): return v * 2.20462 if fwd else v / 2.20462
def grams_ounces(v, fwd=True): return v * 0.035274 if fwd else v / 0.035274
def litres_gallons(v, fwd=True): return v * 0.264172 if fwd else v / 0.264172
def ml_floz(v, fwd=True): return v * 0.033814 if fwd else v / 0.033814
def atm_pascals(v, fwd=True): return v * 101325 if fwd else v / 101325
def bar_psi(v, fwd=True): return v * 14.5038 if fwd else v / 14.5038
def joules_calories(v, fwd=True): return v * 0.239006 if fwd else v / 0.239006
def kwh_joules(v, fwd=True): return v * 3.6e6 if fwd else v / 3.6e6

CHART = {
    "Length": [("m / ft", "m", "ft", metres_feet), ("in / cm", "in", "cm", inches_cm), ("mi / km", "mi", "km", miles_km)],
    "Temperature": [("C / F", "C", "F", celsius_fahrenheit), ("C / K", "C", "K", celsius_kelvin)],
    "Mass": [("kg / lb", "kg", "lb", kg_pounds), ("g / oz", "g", "oz", grams_ounces)],
    "Volume": [("L / gal", "L", "gal", litres_gallons), ("mL / fl oz", "mL", "fl oz", ml_floz)],
    "Pressure": [("atm / Pa", "atm", "Pa", atm_pascals), ("bar / psi", "bar", "psi", bar_psi)],
    "Energy": [("J / cal", "J", "cal", joules_calories), ("kWh / J", "kWh", "J", kwh_joules)],
}

def choose(prompt, options):
    for i, label in enumerate(options, 1):
        print(f"  {i}) {label}")
    while True:
        pick = input(prompt)
        if pick.isdigit() and 1 <= int(pick) <= len(options):
            return int(pick) - 1
        print("Invalid choice.")

while True:
    kind = list(CHART)[choose("Unit type: ", list(CHART))]
    label, a, b, func = CHART[kind][choose("Conversion: ", [c[0] for c in CHART[kind]])]
    fwd = choose("Direction: ", [f"{a} to {b}", f"{b} to {a}"]) == 0
    try:
        value = float(input("Value: "))
    except ValueError:
        print("Not a number.")
        continue
    src, dst = (a, b) if fwd else (b, a)
    print(f"{value:g} {src} = {func(value, fwd):.4f} {dst}")
    if input("Another conversion? (y/n): ").lower() != "y":
        break

# Task - 3, Palindrome Checker
def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

for word in ["civic", "radar", "level", "rotor", "kayak", "madam", "refer",
             "rotator", "deified", "racecar", "reviver", "python"]:
    print(f"{word}: {is_palindrome(word)}")
print(is_palindrome("A man, a plan, a canal: Panama"))  # True

# Task - 4, Text Compression
def compress_string(text):
    if not text:
        return text
    parts = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            parts.append(f"{text[i - 1]}{count}")
            count = 1
    parts.append(f"{text[-1]}{count}")
    compressed = "".join(parts)
    return text if len(compressed) > len(text) else compressed

print(compress_string("aaabbbbcccddeee"))  # a3b4c3d2e3
print(compress_string("Hello"))            # Hello

# Task - 5, Lambda Rewrite (Quiz)
from random import randint
ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b else None,
    "**": lambda a, b: a ** b,
    "%": lambda a, b: a % b if b else None,
}
new_question = lambda: (randint(0, 9), randint(0, 9))
is_correct = lambda given, expected: abs(given - expected) < 0.01
get_number = lambda prompt: float(input(prompt))

score = 0
asked = 0
while True:
    symbol = input("Operation (+ - * / ** %) or q to quit: ")
    if symbol == "q":
        break
    if symbol not in ops:
        print("Invalid operation.")
        continue
    a, b = new_question()
    expected = ops[symbol](a, b)
    if expected is None:
        print("Error: division by zero. New question.")
        continue
    try:
        given = get_number(f"What is {a} {symbol} {b}? ")
    except ValueError:
        print("Please enter a number.")
        continue
    asked += 1
    if is_correct(given, expected):
        score += 1
        print("Correct!")
    else:
        print(f"Wrong - the answer is {expected:.2f}")
print(f"Final score: {score}/{asked}")

# Task - 7, Pure Python EDA - Mini Statistics Report
import statistics as stats
try:
    values = [float(v) for v in input("Enter five numbers (space-separated): ").split()]
    if len(values) != 5:
        print("Please enter exactly five numbers.")
    else:
        print("Values: " + ", ".join(f"{v:g}" for v in values))
        print(f"Total = {sum(values):.2f}")
        print(f"Mean = {stats.mean(values):.2f}")
        print(f"Median = {stats.median(values):.2f}")
        print(f"Std Dev = {stats.stdev(values):.2f}")
except ValueError:
    print("Please enter numbers only.")

# Task - 10, Pentagon Area
from math import tan, pi
s = float(input("Enter the side length: "))
area = 5 * s ** 2 / (4 * tan(pi / 5))
print(f"Area = {area:.2f}")

## Week 4
# Task - 5, Count Range
def countRange(values, minimum, maximum):
    return sum(1 for v in values if minimum <= v < maximum)

print(countRange([1, 2, 3, 4, 5, 6], 2, 5))          # 3
print(countRange([1.5, 2.5, 3.5, 4.5], 2.0, 4.0))    # 2
print(countRange([5, 5, 5], 5, 6))                   # 3
print(countRange([], 0, 10))                         # 0

# Task - 6, Sublist
def isSublist(larger, smaller):
    if not smaller:
        return True
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False

print(isSublist([1, 2, 3, 4], [2, 3]))        # True
print(isSublist([1, 2, 3, 4], [2, 4]))        # False
print(isSublist([1, 2, 3, 4], []))            # True
print(isSublist([1, 2, 3, 4], [1, 2, 3, 4]))  # True
print(isSublist([1, 2], [1, 2, 3]))           # False

# Task - 7, EDA Challenge - Student Marks Analysis
student_data = [
    [101, "Alice", 85, 92, 88],
    [102, "Bob", 78, 81, 75],
    [103, "Charlie", 90, 85, 89],
    [104, "David", 65, 70, 72],
    [105, "Eve", 88, 95, 90],
]
for row in student_data:
    row.append(round(sum(row[2:5]) / 3, 2))   # average is the new last element
best = max(student_data, key=lambda r: r[5])
worst = min(student_data, key=lambda r: r[5])
print(f"Highest average: {best[1]} ({best[5]})")
print(f"Lowest average: {worst[1]} ({worst[5]})")
above_75 = [r[1] for r in student_data if all(score > 75 for score in r[2:5])]
print("Above 75 in all subjects:", above_75)

# Task - 8, Pure Python EDA - Custom Statistics Functions
def get_mean(data):
    return sum(data) / len(data)

def get_median(data):
    ordered = sorted(data)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2   # even length: average the middle two

def get_std(data):
    m = get_mean(data)
    return (sum((x - m) ** 2 for x in data) / (len(data) - 1)) ** 0.5

regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]
for label, data in (("Regular", regular_data), ("Outlier", outlier_data)):
    print(f"{label}: mean={get_mean(data):.1f}, median={get_median(data)}, std={get_std(data):.1f}")
# The outlier drags the mean to 235 but the median stays at 45
print(get_median([1, 2, 3, 4]))  # 2.5

# Task - 25, Managing Study Groups
# Dictionary of sets: dict gives instant lookup by student, set stops duplicate groups
# and makes joining/leaving simple.
groups = {"John": {"Math", "Physics"}, "Emily": {"Physics", "Biology"}, "Alex": {"Math"}}

def join_group(student, group):
    groups.setdefault(student, set()).add(group)

def leave_group(student, group):
    if group in groups.get(student, set()):
        groups[student].remove(group)
    else:
        print(f"{student} is not in {group}.")

def show_groups(student):
    if student not in groups:
        print(f"{student} not found.")
    else:
        print(f"{student}: {', '.join(sorted(groups[student])) or 'no groups'}")

join_group("Alex", "Physics")
join_group("Sam", "Biology")
leave_group("John", "Math")
leave_group("John", "Chemistry")
for name in ("Alex", "John", "Sam", "Zoe"):
    show_groups(name)

# Task - 32, Pure Python EDA - Custom File Parser
import csv

def to_number(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text.strip()

def parse_csv_to_dicts(filepath):
    with open(filepath, newline="") as f:
        return [{key: to_number(value) for key, value in row.items()}
                for row in csv.DictReader(f)]

try:
    data = parse_csv_to_dicts("DATA/sample_data.csv")
    print(f"Rows: {len(data)}")
    for column in data[0]:
        values = [r[column] for r in data]
        if all(isinstance(v, (int, float)) for v in values):
            print(f"{column}: min={min(values)}, max={max(values)}, mean={sum(values) / len(values):.2f}")
        else:
            print(f"{column}: {len(set(values))} unique values")
except FileNotFoundError:
    print("File not found: DATA/sample_data.csv")

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

## Week 6
# Task - 8, Course Statistics with Groupby
import pandas as pd
df = pd.read_csv("DATA/students.csv")
course_stats = (
    df.groupby("Course")
      .agg(Count=("Name", "count"),
           Avg_Grade=("Grade", "mean"),
           Max_Grade=("Grade", "max"),
           Avg_Attendance=("Attendance", "mean"))
      .round({"Avg_Grade": 1, "Avg_Attendance": 1})
      .sort_values("Avg_Grade", ascending=False)
)
print(course_stats)

# Task - 9, Handling Missing Data
import pandas as pd
missing = pd.read_csv("DATA/students_missing.csv")
print(missing.isnull().sum())
print(missing[missing.isnull().any(axis=1)])
missing["Grade"] = missing["Grade"].fillna(round(missing["Grade"].mean(), 1))
missing["Scholarship"] = missing["Scholarship"].fillna("Unknown")
missing["Course"] = missing["Course"].fillna("Unknown")
missing = missing.dropna(subset=["Attendance", "Age"])
print(missing.isnull().sum())   # all zeros
missing.to_csv("DATA/students_clean.csv", index=False)

# Task - 12, City Performance Report
import pandas as pd
df = pd.read_csv("DATA/students.csv")
overall_avg = df["Grade"].mean()
city_report = df.groupby("City").agg(
    Students=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate=("Grade", lambda g: (g >= 60).mean() * 100),
)
city_report["Performance"] = city_report["Avg_Grade"].apply(
    lambda g: "Above Average" if g > overall_avg else "Below Average")
city_report = city_report.round(1).reset_index().sort_values("Avg_Grade", ascending=False)
city_report.to_csv("DATA/city_report.csv", index=False)
print(city_report.to_string(index=False))

# Task - 14, Full EDA Report
import pandas as pd
df = pd.read_csv("DATA/students.csv")
df["Result"] = df["Grade"].apply(lambda g: "Pass" if g >= 60 else "Fail")
# Assumes Scholarship holds Yes/No (or True/False)
df["Has_Scholarship"] = df["Scholarship"].astype(str).str.strip().str.lower().isin(["yes", "true", "y", "1"])

print("Most popular course:", df["Course"].value_counts().idxmax())
print("\nTop 3 students:")
print(df.nlargest(3, "Grade")[["Name", "Course", "Grade"]].to_string(index=False))
print("\nAverage attendance (Pass vs Fail):")
print(df.groupby("Result")["Attendance"].mean().round(1))

corr = df["Attendance"].corr(df["Grade"])
strength = "strong" if abs(corr) >= 0.7 else "moderate" if abs(corr) >= 0.4 else "weak"
direction = "positive" if corr > 0 else "negative"
print(f"\nCorrelation (Attendance vs Grade): {corr:.2f} -> {strength} {direction} relationship")
# Close to 1.0 = strong positive, close to 0 = no relationship, close to -1.0 = strong negative

report = df.groupby("Course").agg(
    Student_Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate_Pct=("Grade", lambda g: (g >= 60).mean() * 100),
    Scholarship_Pct=("Has_Scholarship", lambda s: s.mean() * 100),
).round(1).reset_index()
report.to_csv("DATA/eda_report.csv", index=False)
print("\n" + report.to_string(index=False))

## Week 7
# Task - 9, Word Frequency Counter
def word_frequency(text):
    text = text.lower()
    for mark in ".,!?":
        text = text.replace(mark, "")
    frequency = {}
    for word in text.split():
        frequency[word] = frequency.get(word, 0) + 1
    top5 = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:5]
    print("Top 5 words:")
    for word, count in top5:
        print(f"  {word}: {count}")
    return frequency

text = """Data science is the study of data. Data scientists use data to find patterns.
Machine learning is a part of data science. Scientists study data every day!
The science of data is growing, and data is everywhere."""
word_frequency(text)

try:
    with open("DATA/Les_Brown.txt") as f:
        word_frequency(f.read())
except FileNotFoundError:
    print("DATA/Les_Brown.txt not found")

# Task - 11, Caesar Cipher Encoder and Decoder
def shift_text(text, key):
    result = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + key) % 26 + base))   # % 26 wraps z -> a
        else:
            result.append(ch)
    return "".join(result)

def encode(text, key):
    return shift_text(text, key)

def decode(text, key):
    return shift_text(text, -key)

original = "Hello World! 123"
key = 5
encoded = encode(original, key)
decoded = decode(encoded, key)
print(f"Original: {original}")
print(f"Encoded:  {encoded}")
print(f"Decoded:  {decoded}")
print("Round trip OK:", decoded == original)

# Task - 12, Text Data Cleaning Pipeline
def clean_dataset(records):
    valid_records = []
    invalid_records = []
    for raw in records:
        fields = [f.strip() for f in raw.split("|")]
        if len(fields) != 4 or not all(fields):
            invalid_records.append((raw.strip(), "Empty or missing field"))
            continue
        name, age, email, country = fields
        name = " ".join(name.split()).title()
        if not (age.isdigit() and 18 <= int(age) <= 120):
            invalid_records.append((name, f"Invalid age: {age}"))
            continue
        at = email.find("@")
        if at == -1 or email.find(".", at) == -1:
            invalid_records.append((name, f"Invalid email: {email}"))
            continue
        valid_records.append({"name": name, "age": int(age), "email": email, "country": country.upper()})
    return valid_records, invalid_records
raw_data = [
    "  john SMITH  | 25 | john.smith@email.com | united kingdom ",
    "  MARY  johnson | abc | mary@email | france",
    " | 30 | test@test.com | germany",
    "  bob wilson  | 17 | bob@mail.com | spain  ",
    "  alice Brown  | 28 | alice.b@data.org | italy  ",
    "charlie DAVIS | 35 | | usa",
]
valid_records, invalid_records = clean_dataset(raw_data)
print("VALID")
for record in valid_records:
    print(" ", record)
print("INVALID")
for record, reason in invalid_records:
    print(f"  {record!r} -> {reason}")

# Task - 14, Build a Simple Search Engine
def search(documents, query):
    words = query.lower().split()
    results = []
    for doc in documents:
        tokens = [t.strip(".,!?") for t in doc.lower().split()]
        found = {w: tokens.count(w) for w in words if tokens.count(w) > 0}
        score = sum(found.values())
        if score:
            results.append((score, doc, found))
    results.sort(key=lambda r: r[0], reverse=True)
    print(f"\nResults for '{query}':")
    if not results:
        print("  No matches.")
    for score, doc, found in results:
        matched = ", ".join(f"{w} x{c}" for w, c in found.items())
        print(f"  [score {score}] {doc}")
        print(f"      matched: {matched}")
    return results
documents = [
    "Python is a great programming language for data science and machine learning",
    "Data analysis with Python involves cleaning and processing large datasets",
    "Machine learning models can predict outcomes from historical data",
    "Web development with JavaScript and HTML is different from data work",
    "Python data science libraries include NumPy and Pandas for data processing",
]
search(documents, "data science")
search(documents, "Python machine learning")

## Week 8
# Task - 5, Slow Requests and Retries
import time
import requests

try:
    requests.get("https://httpbin.org/delay/5", timeout=2)
except requests.exceptions.Timeout:
    print("The request timed out.")
def get_with_retry(url, attempts=3):
    for attempt in range(1, attempts + 1):
        try:
            response = requests.get(url, timeout=2)
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(f"Attempt {attempt}/{attempts} timed out.")
            if attempt < attempts:
                time.sleep(2 ** (attempt - 1))   # exponential backoff: 1s, 2s, ...
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
            return None
    print(f"Giving up after {attempts} attempts.")
    return None

get_with_retry("https://httpbin.org/delay/5")

# Task - 7, Regex Basics
import re
text = "Contact Ann on 07123 456789 or ann@mail.com. Bob: bob@work.org, 07987 654321."
match = re.search(r"07\d{3} \d{6}", text)
print("First phone:", match.group() if match else "none found")
print("Emails:", re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+", text))
print("Masked:", re.sub(r"\d", "*", text))

# Task - 8, Pure Python EDA - Text Extractor
import re
import ipaddress

log_data = "User 192.168.1.1 logged in. Failed login from 10.0.0.55. Connection closed by 192.168.1.1."
def is_valid_ip(candidate):
    try:
        ipaddress.ip_address(candidate)   # rejects octets above 255
        return True
    except ValueError:
        return False
candidates = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log_data)
unique_ips = {ip for ip in candidates if is_valid_ip(ip)}
print("Unique IPs:", sorted(unique_ips))
print("Count:", len(unique_ips))

# Task - 9, Refactor into a Class
import requests

class PostClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
    def _get(self, endpoint, params=None):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f"Timed out fetching {endpoint}.")
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error {error.response.status_code} fetching {endpoint}.")
        except requests.exceptions.RequestException as error:
            print(f"Request failed: {error}")
        return None
    def get_post(self, post_id):
        return self._get(f"posts/{post_id}")
    def get_user_posts(self, user_id):
        return self._get("posts", params={"userId": user_id})

client = PostClient("https://jsonplaceholder.typicode.com")
post = client.get_post(1)
if post:
    print(f"Post 1: {post['title']}")
user_posts = client.get_user_posts(3)
if user_posts is not None:
    print(f"User 3 has {len(user_posts)} posts")
## Week 9
# Task - 1, Write generate_hash()
import bcrypt

def generate_hash(psw):
    hashed = bcrypt.hashpw(psw.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")
hash1 = generate_hash("Magic123")
hash2 = generate_hash("Magic123")
print(hash1)
print(hash2)
print("Hashes identical:", hash1 == hash2)   # False, different salts

# Task - 2, Write is_valid_hash()
def is_valid_hash(psw, hash_str):
    return bcrypt.checkpw(psw.encode("utf-8"), hash_str.encode("utf-8"))
print(is_valid_hash("Magic123", hash1))   # True
print(is_valid_hash("Wrong123", hash1))   # False

# Task - 3, Register and Login with File I/O
import os
def register_user(name, password, filepath="lab_users.txt"):
    if not name or "," in name:
        print("Invalid username.")
        return False
    if os.path.exists(filepath):
        with open(filepath) as f:
            if any(line.split(",", 1)[0] == name for line in f):
                print(f"{name} already exists.")
                return False
    with open(filepath, "a") as f:
        f.write(f"{name},{generate_hash(password)}\n")
    return True
def login_user(name, password, filepath="lab_users.txt"):
    if not os.path.exists(filepath):
        return False
    with open(filepath) as f:
        for line in f:
            stored_name, _, stored_hash = line.strip().partition(",")
            if stored_name == name and is_valid_hash(password, stored_hash):
                return True
    return False
if os.path.exists("lab_users.txt"):
    os.remove("lab_users.txt")   # start clean so the demo can be re-run
register_user("alice", "AlicePass1!")
register_user("bob", "BobPass2!")
print(login_user("alice", "AlicePass1!"))   # True
print(login_user("alice", "wrong"))         # False
print(login_user("mallory", "anything"))    # False

# Task - 4, Reflection Questions
# 1. bcrypt generates a new random salt on every call and stores it inside the hash,
#    so the same password produces a different string each time.
# 2. No. Each user gets a different salt, so identical passwords give different hashes.
#    An attacker cannot tell who shares a password and precomputed rainbow tables are useless.
# 3. == on two hashes always fails for a correct password because the salt differs each time.
#    checkpw() reads the salt from the stored hash, re-hashes the attempt and compares properly.

## Week 10
# Task - 1 & 2, Create the Database and users Table
import os
import sqlite3

DB_FILE = "lab_week9.db"
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)   # "recreate" the database
conn = sqlite3.connect(DB_FILE)
conn.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    )
""")
conn.commit()

# Task - 3, INSERT (add_user)
import bcrypt

def add_user(conn, username, password_hash, role="user"):
    conn.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role),
    )
    conn.commit()
def hash_pw(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
add_user(conn, "alice", hash_pw("AlicePass1!"), "admin")
add_user(conn, "bob", hash_pw("BobPass2!"))
add_user(conn, "charlie", hash_pw("CharliePass3!"))

# Task - 4, SELECT
def get_all_users(conn):
    return conn.execute("SELECT * FROM users").fetchall()
def get_user(conn, username):
    return conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
print(len(get_all_users(conn)), "users")
print(get_user(conn, "alice")[:2])
print(get_user(conn, "nobody"))   # None

# Task - 5, UPDATE and DELETE
def update_role(conn, username, new_role):
    cursor = conn.execute("UPDATE users SET role = ? WHERE username = ?", (new_role, username))
    conn.commit()
    return cursor.rowcount
def delete_user(conn, username):
    cursor = conn.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    return cursor.rowcount
update_role(conn, "bob", "moderator")
delete_user(conn, "charlie")
for user_id, username, _, role in get_all_users(conn):
    print(user_id, username, role)

# Task - 6, SQL Injection Demonstration
def get_user_unsafe(conn, username):
    query = f"SELECT * FROM users WHERE username = '{username}'"   # NEVER do this
    print("Query run:", query)
    return conn.execute(query).fetchall()
print(len(get_user_unsafe(conn, "alice")))           # 1 row
print(len(get_user_unsafe(conn, "' OR '1'='1")))     # every row: the condition is always true
print(get_user(conn, "' OR '1'='1"))                 # None: safe version treats it as plain text
# With an f-string the input becomes part of the SQL itself, so an attacker can change the query.
# Parameterised queries (?) send the input separately as data, so it can never be run as SQL.

# Task - 7, Load CSV Data with Pandas
import pandas as pd

pd.DataFrame({
    "incident_id": [1, 2, 3],
    "severity": ["High", "Critical", "Low"],
    "category": ["Phishing", "Ransomware", "Policy"],
    "status": ["Open", "Investigating", "Closed"],
    "description": ["Credential phishing email reported by finance",
                    "Ransomware detected on file server",
                    "Unapproved software installed on laptop"],
}).to_csv("sample_incidents.csv", index=False)
incidents = pd.read_csv("sample_incidents.csv")
incidents.to_sql("cyber_incidents", conn, if_exists="replace", index=False)
print(pd.read_sql("SELECT * FROM cyber_incidents", conn))

# Task - 8, Reflection Questions
# 1. fetchone() returns the next single row (or None); fetchall() returns every remaining row as a list.
# 2. Every row in the table would be deleted, because there is no WHERE clause to limit it.
# 3. If the table already exists, to_sql raises an error by default. if_exists tells pandas whether to
#    'replace' it, 'append' to it, or 'fail'.
conn.close()

## Week 11
# Task - 3, Login Page
# File: Home.py
import hmac
import streamlit as st

st.set_page_config(page_title="Login")
USERS = {
    "alice": {"password": "admin123", "role": "admin"},
    "bob": {"password": "user123", "role": "user"},
}
for key, default in {"logged_in": False, "username": None, "role": None}.items():
    st.session_state.setdefault(key, default)
if st.session_state.logged_in:
    st.switch_page("pages/1_Dashboard.py")
st.title("Login")
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Log in")
if submitted:
    user = USERS.get(username)
    if user and hmac.compare_digest(user["password"].encode(), password.encode()):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user["role"]
        st.switch_page("pages/1_Dashboard.py")
    else:
        st.error("Invalid credentials")

# Task - 4, Protected Dashboard Page
# File: pages/1_Dashboard.py
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard")
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()
st.title("Security Dashboard")
st.write(f"Welcome, {st.session_state.username} ({st.session_state.role})")
incidents = pd.DataFrame({
    "severity": ["High", "Critical", "Low", "Medium", "Critical", "High"],
    "category": ["Phishing", "Ransomware", "Policy", "Malware", "Phishing", "DDoS"],
    "status": ["Open", "Open", "Closed", "Investigating", "Closed", "Open"],
})
col1, col2, col3 = st.columns(3)
col1.metric("Total incidents", len(incidents))
col2.metric("Open", int((incidents["status"] == "Open").sum()))
col3.metric("Critical", int((incidents["severity"] == "Critical").sum()))
st.bar_chart(incidents["category"].value_counts())
st.dataframe(incidents)
with st.sidebar:
    if st.button("Logout"):
        st.session_state.clear()
        st.switch_page("Home.py")

# Task - 6, 7 & 8, Interactive Filters, Layout and Caching
# File: pages/2_Students.py
import pandas as pd
import streamlit as st
st.set_page_config(page_title="Students")
if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()
# Streamlit reruns the whole script on every widget change. @st.cache_data stores the
# returned DataFrame, so the CSV is read from disk once instead of on every rerun.
@st.cache_data
def load_data():
    return pd.read_csv("DATA/students.csv")
df = load_data()
st.sidebar.header("Filters")
city = st.sidebar.selectbox("City", ["All"] + sorted(df["City"].dropna().unique()))
lowest, highest = int(df["Grade"].min()), int(df["Grade"].max())
min_grade = st.sidebar.slider("Minimum grade", lowest, highest, lowest)
filtered = df[df["Grade"] >= min_grade]
if city != "All":
    filtered = filtered[filtered["City"] == city]
st.title("Student Data")
col1, col2, col3 = st.columns(3)
col1.metric("Students", len(filtered))
col2.metric("Average grade", f"{filtered['Grade'].mean():.1f}" if len(filtered) else "N/A")
col3.metric("Average attendance", f"{filtered['Attendance'].mean():.1f}" if len(filtered) else "N/A")

tab_table, tab_charts = st.tabs(["Table", "Charts"])
with tab_table:
    st.dataframe(filtered)
with tab_charts:
    if len(filtered):
        st.bar_chart(filtered.groupby("Course")["Grade"].mean())
    else:
        st.info("No students match the filters.")

# Task - 9, Reflection Questions
# 1. Streamlit reruns the script from the top on every interaction, which resets normal variables.
#    st.session_state survives reruns, so login status and chat history persist.
# 2. st.stop() halts the script at that point, so nothing below (the protected content) is shown.
# 3. st.form() groups the inputs and only reruns the app when the submit button is pressed,
#    instead of rerunning on every keystroke or widget change.

## Week 12
# Task - 3, Multi-Turn Console Chat
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()          # reads OPENAI_API_KEY from .env (never commit this file)
client = OpenAI()
def run_console_chat(system_prompt, client):
    messages = [{"role": "system", "content": system_prompt}]
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            break
        if not user_input:
            continue
        messages.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        except Exception as error:
            print(f"API error: {error}")
            messages.pop()   # keep the history consistent after a failed call
            continue
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print(f"AI: {reply}")
run_console_chat("You are a helpful assistant.", client)

# Task - 4, Prompt Engineering
SYSTEM_PROMPTS = {
    "Cybersecurity": (
        "You are a senior incident response analyst. "
        "Structure every answer as: 1) Summary, 2) Likely cause, 3) Immediate actions, 4) Prevention. "
        "Prioritise containment, then evidence preservation, then recovery. "
        "Give a clear risk rating, reference MITRE ATT&CK where relevant and never invent indicators."
    ),
    "Data Science": (
        "You are an experienced data scientist and ML engineer. "
        "Structure every answer as: 1) Approach, 2) Method, 3) Steps or code, 4) Caveats. "
        "Prioritise data quality, correct statistics and reproducibility, and state your assumptions."
    ),
    "IT Operations": (
        "You are an IT operations lead. "
        "Structure every answer as: 1) Impact, 2) Diagnosis, 3) Fix, 4) Follow-up. "
        "Prioritise service availability, low-risk changes and a documented rollback plan."
    ),
}
for domain, prompt in SYSTEM_PROMPTS.items():
    print(f"{domain}: {len(prompt)} characters")

# Task - 5, Combining Database Data with AI
incident = {
    "id": "INC-2026-014",
    "severity": "High",
    "category": "Phishing",
    "status": "Open",
    "description": "Finance staff received emails impersonating the CEO asking for urgent payments. "
                   "Two users clicked the link and entered credentials.",
}
def build_incident_prompt(incident):
    return (
        "Analyse the following security incident.\n\n"
        f"ID: {incident['id']}\n"
        f"Severity: {incident['severity']}\n"
        f"Category: {incident['category']}\n"
        f"Status: {incident['status']}\n"
        f"Description: {incident['description']}\n\n"
        "Provide:\n"
        "1. Root cause analysis\n"
        "2. Immediate containment actions (bullet points)\n"
        "3. Long-term prevention measures\n"
        "4. Risk assessment (Low / Medium / High / Critical)"
    )
prompt = build_incident_prompt(incident)
print(prompt)
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPTS["Cybersecurity"]},
                  {"role": "user", "content": prompt}],
    )
    print(response.choices[0].message.content)
except Exception as error:
    print(f"API error: {error}")

# Task - 6, Streamlit Chat Page
# File: pages/4_AI_Assistant.py
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Assistant")

if not st.session_state.get("logged_in", False):
    st.warning("Please log in first.")
    st.switch_page("Home.py")
    st.stop()

PROMPTS = {
    "Cybersecurity": "You are a senior incident response analyst. Be structured and prioritise containment.",
    "Data Science": "You are an experienced data scientist. Prioritise data quality and correct statistics.",
    "IT Operations": "You are an IT operations lead. Prioritise availability and safe, reversible changes.",
}

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])   # from .streamlit/secrets.toml
st.session_state.setdefault("ai_messages", [])

with st.sidebar:
    domain = st.selectbox("Domain", list(PROMPTS))
    counter = st.empty()
    if st.button("Clear Chat"):
        st.session_state.ai_messages = []
        st.rerun()

st.title("AI Assistant")
for message in st.session_state.ai_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_text := st.chat_input("Ask a question..."):
    st.session_state.ai_messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        reply = ""
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": PROMPTS[domain]}] + st.session_state.ai_messages,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    reply += chunk.choices[0].delta.content
                    placeholder.markdown(reply + "|")
            placeholder.markdown(reply)
            st.session_state.ai_messages.append({"role": "assistant", "content": reply})
        except Exception as error:
            placeholder.error(f"API error: {error}")
counter.metric("Messages", len(st.session_state.ai_messages))
