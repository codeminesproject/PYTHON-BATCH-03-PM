
from datetime import datetime,date

str_date = "23/08/2026"

date_datetime = datetime.strptime(str_date,"%d/%m/%Y")
print("datetime:",date_datetime)