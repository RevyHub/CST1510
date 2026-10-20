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

