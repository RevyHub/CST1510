"""
RECORD CHECK  -  my version
===========================
Name:   Thomas Browne
Lane:   Cyber
Date:   16/10/2026
"""
from pathlib import Path
BASE = Path(__file__).parent

# FUNCTIONS
def check_record(value, limit):
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    print(f"{label:<24} value={value:<7g} limit={limit:<7g} "
          f"diff={difference:+8.1f}  {percent:6.1f}%  {status}")

def print_summary(over_count, total):
    print(f"\n{over_count} of {total} records OVER LIMIT")

# STORE
def load_records(filename):
    records = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records

def write_results(filename, results):
    with open(filename, "w") as f:
        for label, status in results:
            f.write(f"{label},{status}\n")

records = load_records(BASE / "records.txt")

# PROCESS + OUTPUT
over_count = 0
results = []
for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_count += 1
print_summary(over_count, len(records))
write_results(BASE / "results.txt", results)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#        Error: (paste the FileNotFoundError message here)
#    [ ] Check every function still does one job