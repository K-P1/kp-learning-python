date and time in python:
date- manipulate just date(month,day,year)
time- manipulates time independent of the day(hour,minute,second and microsecond)
datetime- combination of time and date(month,day year,hour,second,microsecond)
timedelta- a duration of time used for manipulating dates
tzinfo- an abstract class fordealing with time zone
*befor using date in pyton import this 3:
from datetime import datetime
from datetime import date
from datetime import time
*functions under datetime module
date.today()____todays date
date.today().day____ current day calender number
date.today().month____current month
date.today().year____current year
date.today().weekday____
*value btw 0-6 where 0 is monday and 6 is sunday
datetime.now()____current date and time
datetime.(datetime.now())____current time

