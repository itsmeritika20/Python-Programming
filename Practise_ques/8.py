#linear search
def linear_Search(list, n, key):  
    for i in range(0, n):  
        if (list[i] == key):  
            return i  
    return -1  
list = [1 ,3, 5, 4, 7, 9]  
key = int(input("\nEnter value of key:"))  
n = len(list)  
result = linear_Search(list, n, key)  
if(result == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", result)
