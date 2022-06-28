from datetime import datetime
from datetime import date
now=datetime.now()
print("The current time is",now.strftime("%H:%M:%S"))
now1=date.today()
print("The current day is",now1)