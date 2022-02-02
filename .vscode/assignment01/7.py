#Write a program to print all prime numbers from 1 to 300.

lower = 1
upper = 300

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   #all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)