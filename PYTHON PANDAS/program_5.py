
import pandas as pd

df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student_marks.xlsx")

print(df)

df1 = df["Student Name"]
df2 = df[["Maths","English","Science"]]

print(df1)
print(df2)