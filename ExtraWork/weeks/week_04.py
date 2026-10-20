## Week 4
# Task - 5, Count Range
def countRange(values, minimum, maximum):
    return sum(1 for v in values if minimum <= v < maximum)

print(countRange([1, 2, 3, 4, 5, 6], 2, 5))          # 3
print(countRange([1.5, 2.5, 3.5, 4.5], 2.0, 4.0))    # 2
print(countRange([5, 5, 5], 5, 6))                   # 3
print(countRange([], 0, 10))                         # 0

# Task - 6, Sublist
def isSublist(larger, smaller):
    if not smaller:
        return True
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False

print(isSublist([1, 2, 3, 4], [2, 3]))        # True
print(isSublist([1, 2, 3, 4], [2, 4]))        # False
print(isSublist([1, 2, 3, 4], []))            # True
print(isSublist([1, 2, 3, 4], [1, 2, 3, 4]))  # True
print(isSublist([1, 2], [1, 2, 3]))           # False

# Task - 7, EDA Challenge - Student Marks Analysis
student_data = [
    [101, "Alice", 85, 92, 88],
    [102, "Bob", 78, 81, 75],
    [103, "Charlie", 90, 85, 89],
    [104, "David", 65, 70, 72],
    [105, "Eve", 88, 95, 90],
]
for row in student_data:
    row.append(round(sum(row[2:5]) / 3, 2))   # average is the new last element
best = max(student_data, key=lambda r: r[5])
worst = min(student_data, key=lambda r: r[5])
print(f"Highest average: {best[1]} ({best[5]})")
print(f"Lowest average: {worst[1]} ({worst[5]})")
above_75 = [r[1] for r in student_data if all(score > 75 for score in r[2:5])]
print("Above 75 in all subjects:", above_75)

# Task - 8, Pure Python EDA - Custom Statistics Functions
def get_mean(data):
    return sum(data) / len(data)

def get_median(data):
    ordered = sorted(data)
    mid = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2   # even length: average the middle two

def get_std(data):
    m = get_mean(data)
    return (sum((x - m) ** 2 for x in data) / (len(data) - 1)) ** 0.5

regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]
for label, data in (("Regular", regular_data), ("Outlier", outlier_data)):
    print(f"{label}: mean={get_mean(data):.1f}, median={get_median(data)}, std={get_std(data):.1f}")
# The outlier drags the mean to 235 but the median stays at 45
print(get_median([1, 2, 3, 4]))  # 2.5

# Task - 25, Managing Study Groups
# Dictionary of sets: dict gives instant lookup by student, set stops duplicate groups
# and makes joining/leaving simple.
groups = {"John": {"Math", "Physics"}, "Emily": {"Physics", "Biology"}, "Alex": {"Math"}}

def join_group(student, group):
    groups.setdefault(student, set()).add(group)

def leave_group(student, group):
    if group in groups.get(student, set()):
        groups[student].remove(group)
    else:
        print(f"{student} is not in {group}.")

def show_groups(student):
    if student not in groups:
        print(f"{student} not found.")
    else:
        print(f"{student}: {', '.join(sorted(groups[student])) or 'no groups'}")

join_group("Alex", "Physics")
join_group("Sam", "Biology")
leave_group("John", "Math")
leave_group("John", "Chemistry")
for name in ("Alex", "John", "Sam", "Zoe"):
    show_groups(name)

# Task - 32, Pure Python EDA - Custom File Parser
import csv
from pathlib import Path

def to_number(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text.strip()

def parse_csv_to_dicts(filepath):
    with open(filepath, newline="") as f:
        return [{key: to_number(value) for key, value in row.items()}
                for row in csv.DictReader(f)]

try:
    data_path = Path(__file__).resolve().parents[1] / "DATA" / "sample_data.csv"
    data = parse_csv_to_dicts(data_path)
    print(f"Rows: {len(data)}")
    if data:
        for column in data[0]:
            values = [row[column] for row in data]
            if all(isinstance(value, (int, float)) for value in values):
                print(f"{column}: min={min(values)}, max={max(values)}, mean={sum(values) / len(values):.2f}")
            else:
                print(f"{column}: {len(set(values))} unique values")
    else:
        print("The CSV file contains no data rows.")
except FileNotFoundError:
    print(f"File not found: {data_path}")

