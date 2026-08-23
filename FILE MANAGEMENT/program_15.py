import os

location = "C:\\CodeMines\\files\\Batch 03 PM"

if os.path.isdir(location):
    print("Folder already created")
else:
    os.makedirs(location)
    print("folder created")