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

