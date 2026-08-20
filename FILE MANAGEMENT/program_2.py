
# create a new text file
# open() it is a predefined function which contains location and mode

file = open("C:\\CodeMines\\files\\sample.txt","w")
news = ["This is line 1","\nThis is line 2","\nThis is line 3"]
file.writelines(news) 

print("file created")