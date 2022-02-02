#Write a program to find out the minimum of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a<=b and a<=c:
    print("The minimum number is ", a)
elif b<=a and b<=c:
    print("The minimum number is ", b)
else:
    print("The minimum number is ", c)