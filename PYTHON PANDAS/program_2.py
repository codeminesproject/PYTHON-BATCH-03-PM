import pandas

# read data from excel

df=pandas.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student_excel.xlsx")

print(df)
print("datatype:",type(df))

print("---- get column info from dataframe ----")

print(df.head())
print(df.info())

