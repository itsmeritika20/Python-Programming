#sum of n digits in recursive way
def getSum(n):
    if n <= 1:
        return n
    else:
        return n + getSum(n - 1)
    
digit = int(input("\nEnter a number:"))
print(getSum(digit))