#Suppose a list has 15 numbers. Write a program that removes all 
#duplicates from this list.

list = [1,2,4,5,4,9,12,8,9,13,12,14,11,14,15]
result = []
for i in list:
    if i not in result:
        result.append(i)
              
print("The result is ",result)