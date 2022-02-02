#Write a program that swaps the values of variables M and N. You are not allowed 
# to use a third variable. You are not allowed to perform arithmetic on M and N.
x = int(input("\nEnter the value of x: "))  
y = int(input("\nEnter the value of y: "))  
print("Before swapping:",x,y)
x, y = y, x
print("After swapping:",x, y)













'''
x = int(input("\nEnter the value of x: "))  
y = int(input("\nEnter the value of y: "))  
print("\nBefore swapping: %d %d" %(x,y))  
#swapping 
x = x + y     
y = x - y    
x = x - y     
print("\nAfter swapping: %d %d" %(x,y))  
'''
