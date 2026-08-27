
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student_marks.xlsx")

print(df)

print("----- add custum column total with value 300 -----")

df["Total"] = 300

print(df)

print("----- add custum column marks obtained -----")

df["Marks Obtained"] = df["Maths"] + df["English"] + df["Science"]

print(df)

print("----- add custum column percentage -----")

df["percentage"] = (df["Marks Obtained"]/df["Total"])*100

print(df)