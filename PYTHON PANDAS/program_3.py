
import pandas as pd

student_list = [{"id":1,"name":"Supriya"},
                {"id":2,"name":"Vidhi"},
                {"id":3,"name":"Diya"},
                {"id":4,"name":"Shankar"}]

print(student_list)

print("==================================================")

# convert list into dataframe

df = pd.DataFrame(student_list)

df = df.rename(columns={"id":"Student ID","name":"Student Name"})

print(df)

print("==================================================")

# create dexcel from dataframe

df.to_excel("student_data.xlsx",index=False,sheet_name="Student Data")

print("file created")