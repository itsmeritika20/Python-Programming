#list
a = 12
b = "This is string"
c = False
myList = [a, b, c]
print(myList)
print(type(myList))

#list indexing
List = [7, 9, "Harry"]
print(List[2])
print(List[0:2]) #index 2 is not included in list
print(List[0:4])
print(List[0:21]) #as their is no more value so console will print the existing list

#List methods
myListOfNumber = [1, 8, 7, 2, 21, 15, 21]
print(myListOfNumber)

#myListOfNumber.sort()
#sort() function doesn't return anything but it update the original list
#print(myListOfNumber)

#myListOfNumber.reverse()
#reverse() function reverse the original list
#print(myListOfNumber)

#myListOfNumber.append(9)
#append() function add value at the end of the list, not return new list
#print(myListOfNumber)

#myListOfNumber.insert(2, 9)
#insert()function insert value at particular position
#print(myListOfNumber)

#myListOfNumber.pop(2)
#pop() function delete the last element of the list or a particular element
#print(myListOfNumber)

myListOfNumber.remove(21)
#if duplicate item can found in the list the first occurence item removed 
print(myListOfNumber)

