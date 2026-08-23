
from datetime import datetime,timedelta

current_date = datetime.now()

print("current date:",current_date)


date_after_10_days = current_date + timedelta(days=10)
print("date after 10 days:",date_after_10_days)

date_before_10_days = current_date - timedelta(days=10)
print("date before 10 days:",date_before_10_days)