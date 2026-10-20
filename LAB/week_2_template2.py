"""
RECORD CHECK  -  my version
===========================
Name  : Thomas Duaine Browne
Lane  : Cyber
Date  : 30/09/2026
"""
label = input("Enter the IP: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))
difference = value - limit
percent = (difference / limit) * 100
print (f"Difference: {difference:.2f}")
print (f"Percent: {percent:.2f}%")
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
