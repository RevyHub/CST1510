"""
RECORD CHECK  -  my version
===========================
Name:   Thomas Browne
Lane:   Cyber
Date:   9/10/2026
"""

# FUNCTIONS
def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    if percent >= 90:
        return "WARNING"
    return "OK"
def check(value, limit):
    difference = limit - value
    percent = value / limit * 100
    return difference, percent
def read_number(prompt, must_be_positive=False):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if must_be_positive and number <= 0:
            print("Must be greater than 0.")
            continue
        return number
def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  {'Value':<12}{value:>20,.2f}")
    print(f"  {'Limit':<12}{limit:>20,.2f}")
    print(f"  {'Difference':<12}{difference:>20,.2f}")
    print(f"  {'Percent':<12}{percent:>19,.2f}%")
    print(f"  {'Status':<12}{status:>20}")
    print("=" * 34)

# MAIN
def main():
    over_limit_count = 0
    records_checked = 0
    while True:
        # INPUT
        label = input("\nLabel (name/hostname/IP, or 'quit'): ").strip()
        if label.lower() == "quit":
            break
        if not label:
            print("  Label cannot be empty.")
            continue
        value = read_number("Current value: ")
        limit = read_number("Limit: ", must_be_positive=True)
        # PROCESS
        difference, percent = check(value, limit)
        status = status_of(percent)
        # OUTPUT
        print_report(label, value, limit, difference, percent, status)
        records_checked += 1
        if status == "OVER LIMIT":
            over_limit_count += 1
    print(f"\nChecked {records_checked} record(s); {over_limit_count} OVER LIMIT.")

if __name__ == "__main__":
    main()

# ==========================================================================
# 5. Checklist:
#
#    [x] Run it three times with different numbers
#    [x] Limit of 0: would raise ZeroDivisionError in check(); input validation
#        now rejects limits <= 0 so it can't happen
#    [x] Every function does one job - check() calculates, print_report()
#        prints, read_number() reads input, status_of() classifies