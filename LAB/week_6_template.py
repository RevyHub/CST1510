"""
RECORD CHECK  -  my version
===========================

Name  : Thomas Browne
Lane  : Cyber
Date  : 3/11/2026
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cyber.csv")

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "Over Limit" if p >= 100
    else "Warning" if p >= 90
    else "Ok"
)
print(df)

print("\nNot Ok Rows:")
print(df[df["status"] != "Ok"])
print("\nCount Per Status:")
print(df["status"].value_counts())
df.to_csv("cyber_reports.csv", index=False)
df["status"].value_counts().plot(kind="bar")
plt.title("Status Counts")
plt.savefig("Status_counts.png")
plt.show()