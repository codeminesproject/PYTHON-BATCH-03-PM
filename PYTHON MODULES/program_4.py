
from arithmatic import division,multiplication
import math
import random

division(45,8)
multiplication(33,44)

num_1 = 5
power = 2

print(f"{num_1} power {power}: {math.pow(num_1,power)}")

num_2 = 89.87
print(f"lower limit of {num_2}: {math.floor(num_2)}")
print(f"upper limit of {num_2}: {math.ceil(num_2)}")

print(f"square root of {num_1}: {math.sqrt(num_1)}")

print("random number between 1 to 100:",random.randint(1,100))
print("random number:",random.random())

list_var = ["Akshay","Supriya","Jansi","Shankar"]

print("choose random:",random.choice(list_var))

random.shuffle(list_var)
print("shuffle data:",list_var)
