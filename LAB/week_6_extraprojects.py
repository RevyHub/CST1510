import pandas as pd

df = pd.read_csv("login_attempts.csv")

print(df.head())
print(df.dtypes)
print(len(df))