num = int(input("Enter number:"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of the number is {factorial}")