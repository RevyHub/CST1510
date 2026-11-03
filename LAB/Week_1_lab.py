"""
RECORD CHECK  -  my version
===========================

Name  : Thomas Browne
Lane  : Cyber
Date  : 25/09/2026
===========================
"""

source_ip = input("Enter source IP: ")
failed_logins = float(input("Enter failed logins: "))
total_attempts = float(input("Enter total attempts: "))

login_difference = failed_logins - total_attempts
remaining_attempts = total_attempts - failed_logins
failure_percentage = (failed_logins / total_attempts) * 100
success_percentage = 100 - failure_percentage

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)
print(f"  Failed      : {failed_logins:>10.2f}")
print(f"  Total       : {total_attempts:>10.2f}")
print(f"  Remaining   : {remaining_attempts:>10.2f}")
print(f"  Percent     : {failure_percentage:>10.2f} %")
print(f"  Difference  : {login_difference:>+10.2f}")
print(f"  Success     : {success_percentage:>10.2f} %")
print("=" * 34)
