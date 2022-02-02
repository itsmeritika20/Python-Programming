#set:collection of unordered elements,but once set is declared it can't change
#len(), add(), remove(), pop(), union(), intersection()
mySet = {1,34,21}
print(mySet)
print(len(mySet))

mySet.add(65)
mySet.add("1") #two 1 are different object in set
print(mySet)

mySet.remove(21) #remove specific element which is given
print(mySet)

mySet.pop() #pop() randomly pop element from set
print(mySet)