#Suppose a date is represented as a tuple (d,m,y). Write a program to 
#create two date tuples and find the number of days between the two dates.

from datetime import date
first_date = date(2021,9,22)
second_date = date(2021,6,2)
day_difference = first_date - second_date
print(day_difference)