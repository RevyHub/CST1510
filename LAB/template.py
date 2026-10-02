"""
RECORD CHECK  -  my version
===========================

Name  : Thomas Duaine Browne
Lane  : Cyber
Date  : 30/09/2026

Run it:   python template.py
Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input("Enter the IP: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))

# 2. Work out the difference and the percentage.       [Typical and above]
difference = value - limit
percent = (difference / limit) * 100
print (f"Difference: {difference:.2f}")
print (f"Percent: {percent:.2f}%")

# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
status = ""
status_Num = 100
if value and limit > int(status_Num):
    status = "OVER LIMIT"
    print(status)
elif value and limit == 90:
    status = "WARNING, close to limit"
    print(status)
else:
    status = "OK"
    print(status)

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

over_limit_count = 0
while True:
    label = input("Record ID: ")
    if label.lower() == "quit":
        break
    value = float(input("Value: "))
    limit = float(input("Limit: "))
    difference = value - limit
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    print("=" * 34)
    print(f"RECORD CHECK\t {label}")
    print("=" * 34)
    print(f"Value:\t{value:>10.2f}")
    print(f"Limit:\t{limit:>10.2f}")
    print(f"Difference:\t{difference:>+10.2f}")
    print(f"Of limit:\t{percent:>9.1f} %")
    print(f"Status:\t{status:>10}")
    print("=" * 34)
    print()
print(f"Done. {over_limit_count} record(s) were OVER LIMIT.")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
