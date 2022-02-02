#Write a program to print all Armstrong numbers between 1 and 500.

lower = 1
upper = 500
print("Armstrong numbers between", lower, "and" ,upper,":")
for num in range(lower,upper + 1):
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)