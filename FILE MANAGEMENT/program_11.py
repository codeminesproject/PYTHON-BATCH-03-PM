
import shutil

old_file_name = "C:\\CodeMines\\files\\my_first_file.txt"
new_file_name = "C:\\CodeMines\\files\\destination\\sample.txt"

shutil.move(old_file_name,new_file_name)
print("file moved")