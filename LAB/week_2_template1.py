"""
RECORD CHECK  -  my version
===========================
Name:	Thomas Browne
Lane:	Cyber
Date:	09/10/2026
"""
def status_of(percent):
	if percent >= 100:
		return "OVER LIMIT"
	elif percent >= 90:
		return "WARNING"
	else:
		return "OK"
def check(value, limit):
	difference = value - limit
	percent = (value / limit) * 100
	return difference, percent
def print_report(label, value, limit, difference, percent, status):
	print()
	print("=" * 34)
	print(f"RECORD CHECK -\t{label}")
	print("=" * 34)
	print(f"Failed logins:\t{value:10.2f}")
	print(f"Total attempts:\t{limit:10.2f}")
	print(f"Difference:\t{difference:10.2f}")
	print(f"Percent:\t{percent:9.2f} %")
	print(f"Status:\t{status:>10}")
	print("=" * 34)
over_limit_count = 0
while True:
	label = input("Source IP (or 'quit' to stop): ").strip()
	if label.lower() == "quit":
		break
	value = float(input("Failed logins:\t"))
	limit = float(input("Total attempts:\t"))
	difference, percent = check(value, limit)
	status = status_of(percent)
	print_report(label, value, limit, difference, percent, status)
	if status == "OVER LIMIT":
		over_limit_count += 1
print(f"OVER LIMIT records: {over_limit_count}")
