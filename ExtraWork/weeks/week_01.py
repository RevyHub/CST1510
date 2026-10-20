## Week 1
# Task - 1, Questionnaire
name = input("Enter your name: ")
interest = input("Enter your interest: ")
nationality = input("Enter your nationality: ")
course = input("Enter your course: ")
experience = input("Enter your programming experience: ")
print("User Information:")
print(f"\tName: {name}")
print(f"\tInterest: {interest}")
print(f"\tNationality: {nationality}")
print(f"\tCourse: {course}")
print(f"\tExperience: {experience}")

# Task - 2, Rectangle Area and Perimiter
width = 4.5
height = 7.9
area = width * height
perimeter = 2 * (width + height)
print(f"The Area is {area}")
print(f"The Perimeter is {perimeter}")

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
print(f"Sum of 1 to {n} = {total}")

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

