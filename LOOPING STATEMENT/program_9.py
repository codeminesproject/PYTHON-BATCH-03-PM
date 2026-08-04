
"""
continue: continue is a keyword used to skip current iteration on specific condition met
"""

for i in range(1,11):
    add = i + 3
    if add == 9:
        continue
    print(i)

print("Program Completed")