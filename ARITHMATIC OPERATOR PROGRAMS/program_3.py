
"""
Write a Python program to input principal amount, rate of interest, and time. 
Calculate and display the simple interest and total amount.

simple interest = (principle * rate of interest * time)/100
total amount = principle + simple interest
"""

principle_amount = 100000
rate_of_interest = 9.5
time = 3

simple_interest = (principle_amount * rate_of_interest * 3)/100
print("Simple Interest:",simple_interest)

total_amount = principle_amount + simple_interest
print("Total Amount:",total_amount)