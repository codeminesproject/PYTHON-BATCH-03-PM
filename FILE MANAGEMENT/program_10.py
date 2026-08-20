
import shutil

old_file_name = "C:\\CodeMines\\files\\my_first_file.txt"
new_file_name = "C:\\CodeMines\\files\\destination\\my_first_file.txt"

shutil.copy(old_file_name,new_file_name)
print("file copied")