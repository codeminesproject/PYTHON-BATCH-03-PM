import pandas as pd

student_df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student.xlsx",sheet_name="Student Data")
course_df = pd.read_excel("C:\\CodeMines\\CodeMines Excel\\PYTHON FILES\\student.xlsx",sheet_name="Course Data")

merge_df = pd.merge(left=student_df,right=course_df,how="right",left_on="Name",right_on="Student Name")

merge_df.to_excel("right_join.xlsx",index=False)

print("file created")