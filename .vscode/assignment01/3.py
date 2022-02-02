#Any year is input through the keyboard. Write a program to determine 
#whether the year is a leap year or not.

year = int(input("Enter the year: "))
if year%4 == 0 and year%100 != 0:
    print("The year is a leap year.")
elif year%100 == 0:
    print("The year is not a leap year.")
elif year%400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")