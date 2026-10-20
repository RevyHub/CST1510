## Week 6
# Task - 8, Course Statistics with Groupby
from pathlib import Path

import pandas as pd

data_path = Path(__file__).resolve().parents[1] / "DATA" / "students.csv"
df = pd.read_csv(data_path)
course_stats = (
    df.groupby("Course")
      .agg(Count=("Name", "count"),
           Avg_Grade=("Grade", "mean"),
           Max_Grade=("Grade", "max"),
           Avg_Attendance=("Attendance", "mean"))
      .round({"Avg_Grade": 1, "Avg_Attendance": 1})
      .sort_values("Avg_Grade", ascending=False)
)
print(course_stats)

# Task - 9, Handling Missing Data
missing_path = data_path.with_name("students_missing.csv")
missing = pd.read_csv(missing_path)
print(missing.isnull().sum())
print(missing[missing.isnull().any(axis=1)])
missing["Grade"] = missing["Grade"].fillna(round(missing["Grade"].mean(), 1))
missing["Scholarship"] = missing["Scholarship"].fillna("Unknown")
missing["Course"] = missing["Course"].fillna("Unknown")
missing = missing.dropna(subset=["Attendance", "Age"])
print(missing.isnull().sum())   # all zeros
missing.to_csv(data_path.with_name("students_clean.csv"), index=False)

# Task - 12, City Performance Report
df = pd.read_csv(data_path)
overall_avg = df["Grade"].mean()
city_report = df.groupby("City").agg(
    Students=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate=("Grade", lambda g: (g >= 60).mean() * 100),
)
city_report["Performance"] = city_report["Avg_Grade"].apply(
    lambda g: "Above Average" if g > overall_avg else "Below Average")
city_report = city_report.round(1).reset_index().sort_values("Avg_Grade", ascending=False)
city_report.to_csv(data_path.with_name("city_report.csv"), index=False)
print(city_report.to_string(index=False))

# Task - 14, Full EDA Report
df = pd.read_csv(data_path)
df["Result"] = df["Grade"].apply(lambda g: "Pass" if g >= 60 else "Fail")
# Assumes Scholarship holds Yes/No (or True/False)
df["Has_Scholarship"] = df["Scholarship"].astype(str).str.strip().str.lower().isin(["yes", "true", "y", "1"])

print("Most popular course:", df["Course"].value_counts().idxmax())
print("\nTop 3 students:")
print(df.nlargest(3, "Grade")[["Name", "Course", "Grade"]].to_string(index=False))
print("\nAverage attendance (Pass vs Fail):")
print(df.groupby("Result")["Attendance"].mean().round(1))

corr = df["Attendance"].corr(df["Grade"])
strength = "strong" if abs(corr) >= 0.7 else "moderate" if abs(corr) >= 0.4 else "weak"
direction = "positive" if corr > 0 else "negative"
print(f"\nCorrelation (Attendance vs Grade): {corr:.2f} -> {strength} {direction} relationship")
# Close to 1.0 = strong positive, close to 0 = no relationship, close to -1.0 = strong negative

report = df.groupby("Course").agg(
    Student_Count=("Name", "count"),
    Avg_Grade=("Grade", "mean"),
    Avg_Attendance=("Attendance", "mean"),
    Pass_Rate_Pct=("Grade", lambda g: (g >= 60).mean() * 100),
    Scholarship_Pct=("Has_Scholarship", lambda s: s.mean() * 100),
).round(1).reset_index()
report.to_csv(data_path.with_name("eda_report.csv"), index=False)
print("\n" + report.to_string(index=False))

