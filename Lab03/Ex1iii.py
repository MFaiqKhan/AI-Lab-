# a Python program to extract year, month, date and time using Lambda.

# import datetime module
import datetime

# datetime object containing current date and time
now = datetime.datetime.now() # why not datetime.now()? datetime is a module, datetime.now() is a function

# use lambda to print year, month, date and time
year = lambda x: x.year
month = lambda x: x.month
date = lambda x: x.day
time = lambda x: x.time()

# print the result
print("Year: ", year(now))
print("Month: ", month(now))
print("Date: ", date(now))
print("Time: ", time(now))