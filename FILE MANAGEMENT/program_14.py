
import os

location = "C:\\CodeMines\\files"

old_file_name = "sample.txt"
old_file_path = os.path.join(location,old_file_name)

isExist = os.path.exists(old_file_path)

print(isExist)