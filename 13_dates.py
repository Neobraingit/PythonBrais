### DATES ###

from datetime import datetime

now = datetime.now()

print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)

timestamp = now.timestamp()
print (timestamp)

year_2023 = datetime(2023, 2, 26) # Creamos una fecha

def print_date (date):
    print (date.year)
    print (date.month)
    print (date.day)
    print (date.hour)
    print (date.minute)
    print (date.second) 
    print (date.timestamp())
    
print_date(year_2023)

from datetime import time

current_time = time(10, 32, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)



