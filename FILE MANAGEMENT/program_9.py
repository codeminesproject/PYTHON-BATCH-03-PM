
import os

old_file_name = "C:\\CodeMines\\files\\sample.txt"
new_file_name = "C:\\CodeMines\\files\\my_first_file.txt"

os.rename(old_file_name,new_file_name)
print("file renamed")