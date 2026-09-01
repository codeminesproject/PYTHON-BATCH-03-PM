
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\employee_data.xlsx")

df_1 = df.groupby("City")["Salary"].sum() 

df_1.plot(kind="barh")

plt.ylabel("Sum of Salary")
plt.xlabel("City")
plt.title("City Wise Salary")

plt.show()

