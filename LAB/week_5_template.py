"""
RECORD CHECK  -  my version
===========================

Name  : Thomas Browne
Lane  : Cyber
Date  : 25/10/2026
"""
import os

class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)
        self.limit = float(limit)
        if self.value >= self.limit:
            Record.over_limit_count += 1

    def status(self):
        percentage = (self.value / self.limit) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"
        
print(os.getcwd())
"""This code above is needed as my system is having issues finding the file.
Even though it has access to it"""
def load_records(path):
    records = []
    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, value, limit))
    return records
records = load_records("week_5_records.txt")
for record in records:
    print()
    print("=" * 34)
    print(f"Record Check \t{record.label}")
    print("=" * 34)
    print(f"Value:  {record.value}")
    print(f"Limit:  {record.limit}")
    print(f"Status: {record.status()}")
    print("=" * 34)
print()
print(f"Total Over Limit Records: {Record.over_limit_count}")
