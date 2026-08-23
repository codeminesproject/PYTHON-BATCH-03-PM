
from datetime import datetime

current_date = datetime.now()

print("value of variable current_date:",current_date)
print("datatype of variable current_date:",type(current_date))

# current date: 2026-08-23 12:26:27.092489
# o/p: 23-08-2026

print("----- convert datetime into string format ------")

str_date = current_date.strftime("%d-%m-%Y")

print("value of variable str_date:",str_date)
print("datatype of variable str_date:",type(str_date))

print("----------------------------------------------------")

print("current long year:",current_date.strftime("%Y"))
print("current short year:",current_date.strftime("%y"))

print("current month:",current_date.strftime("%m"))
print("current month in words:",current_date.strftime("%B"))
print("current month in words:",current_date.strftime("%b"))

print("current day:",current_date.strftime("%d"))
print("current day in words:",current_date.strftime("%A"))
print("current day in words:",current_date.strftime("%a"))

print("current hour:",current_date.strftime("%H"))
print("current minutes:",current_date.strftime("%M"))
print("current seconds:",current_date.strftime("%S"))

print("----------------------------------------------------")