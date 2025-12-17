# date time  : 

import  datetime 

"""
a = datetime.datetime.now()
print(a)

b=datetime.datetime.today()
print(b)
"""
# format : 14-12-25  10 :18 :34 

"""
a = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
print(a)
"""

# custom date :

"""a= datetime.datetime(2025,12,14,10,19,34,34567)
print(a)
print(a.day)
print(a.month)
print(a.year)
print(a.hour)
print(a.minute)
print(a.second)
"""

# future :
from datetime import timedelta 
"""
today =datetime.datetime.today() 
future= today + timedelta(days=265)

print("today date is  :",today)
print("future date is  :",future)
"""

import time 

"""a= time.time()
print(a)

b=time.ctime(a)
print(b)
"""

"""c=time.asctime()
print(c)

d=time.localtime()
print(d)

for i in range(10):
    time.sleep(0.1)
    print(i)
"""

# calender : 

"""
import calendar

a=calendar.calendar(2025)
print(a)
"""

# package : 

"""from mypackage import functions as f , hello as h

print(f.mul(23,67))

h.say_hello("rohit")
"""
