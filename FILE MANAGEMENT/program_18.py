import os

location = "C:\\CodeMines\\files\\Batch 03 PM"

file_list = []
folder_list = []

content_list = os.listdir(location)

print("NO of files and folder in directory:",len(content_list))

for i in content_list:
    file_path = os.path.join(location,i)
    if os.path.isfile(file_path):
        file_list.append(i)
    else:
        folder_list.append(i)

print("File List:",file_list)
print("Folder List:",folder_list)

