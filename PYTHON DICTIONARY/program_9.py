
# string key

dict_1 = {"id":1,"name":"CodeMines"}

# number key

dict_1 = {id:1,1:"CodeMines",2:2,3:"Hello"}

print("value of key 1:",dict_1[1])
print("value of key 2:",dict_1[2])
print("value of key 3:",dict_1[3])

# we can use tuple as a key

dict_1 = {"id":1,1:"CodeMines",(45,67,89):"Hello"}

print("value from tuple:",dict_1[(45,67,89)])