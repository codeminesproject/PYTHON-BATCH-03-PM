
import os

location = "C:\\CodeMines\\files"

old_file_name = "sample.txt"
new_file_name = "my_first_file.txt"

old_file_path = os.path.join(location,old_file_name)

print(old_file_path)