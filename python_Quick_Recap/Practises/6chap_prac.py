#find max num out of 4 numbers
num1 = int(input("Enter 1st num:"))
num2 = int(input("Enter 2nd num:"))
num3 = int(input("Enter 3rd num:"))
num4 = int(input("Enter 4th num:"))

if(num1 > num2):
    maxnum1 = num1
else:
    maxnum1 = num2

if(num3 > num4):
    maxnum2 = num3
else:
    maxnum2 = num4

if(maxnum1 > maxnum2):
    maxnum = maxnum1
else:
    maxnum = maxnum2

print("Greatest number is",maxnum)
