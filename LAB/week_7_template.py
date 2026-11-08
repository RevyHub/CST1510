"""
RECORD CHECK - my version
=========================
Name  : Thomas Browne
Lane  : Cyber Security
Date  : 08/11/2026
"""
# My Functions
def parse_line(raw_line):
    """Clean and parse one raw login record."""
    parts = raw_line.strip().upper().split(",")
    ip = parts[0].split("=")[1].strip()
    attempts = int(parts[1].split("=")[1].strip())
    result = parts[2].split("=")[1].strip()
    return {
        "ip": ip,
        "attempts": attempts,
        "result": result
    }

def status_of(record):
    """Return FLAGGED or OK based on attempts."""
    if record["attempts"] >= 10:
        return "FLAGGED"
    else:
        return "OK"
# Input
raw_records = [
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    " src=192.168.1.1 , attempts=4 , result=failed ",
    "SRC=10.0.0.9, ATTEMPTS=15, RESULT=FAILED",
    "src=172.16.0.3,attempts=2,result=success",
    " SRC=10.0.0.12 , ATTEMPTS=20 , RESULT=FAILED "
]
# Output
flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)
    print(record, "-", status)
    if status == "FLAGGED":
        flagged_count += 1
print("\nSUMMARY")
print(f"Records processed: {len(raw_records)}")
print(f"Flagged records: {flagged_count}")