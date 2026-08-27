
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\employee_data.xlsx")

print(df)

print("--- city wise total salary ---")

df_1 = df.groupby("City")["Salary"].sum() 

print(df_1)

print("--- city wise total records ---")

df_2 = df.groupby("City")["City"].count()

print(df_2)

print("--- city wise min salary ---")

df_3 = df.groupby("City")["Salary"].min() 

print(df_3)

print("--- city wise max salary ---")

df_4 = df.groupby("City")["Salary"].max() 

print(df_4)

print("--- city wise average salary ---")

df_5 = df.groupby("City")["Salary"].mean() 

print(df_5)

print("--- city wise designation wise total salary ---")

df_6 = df.groupby(["City","Department","Gender"])["Salary"].sum() 

print(df_6)