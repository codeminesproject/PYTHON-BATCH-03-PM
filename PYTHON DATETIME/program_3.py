
from datetime import datetime
import sys

current_date = datetime.now()

print("value of variable current_date:",current_date)
print("datatype of variable current_date:",type(current_date))
print("data size of variable current_date:",sys.getsizeof(current_date))

print("-------------------------------------------------------------------")

print("current year:",current_date.year)
print("current month:",current_date.month)
print("current day:",current_date.day)
print("current hour:",current_date.hour)
print("current minutes:",current_date.minute)
print("current seconds:",current_date.second)
print("current micro seconds:",current_date.microsecond)