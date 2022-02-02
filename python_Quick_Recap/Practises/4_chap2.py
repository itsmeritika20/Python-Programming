#Tuples:list is not changed in the case of tuples.Just like we have strings,
#integers,float tuple is another datatype which cannot be changed
myTuple = (3, 6, 7)
print(myTuple)
print(type(myTuple))

tuple = ()
print(tuple) #empty tuple

MyTuple = (5,)
#if you create a tuple of one item you have to add a comma inside ()
#if you dont add the comma the it will be treated as an integer
print(MyTuple)
print(type(MyTuple))

#tuple methods

#1.count():count the given item
tup1 = (1, 7, 2, 5, 1, 6, 1, 1)
print(tup1.count(1))

#2.index():give the index of given item.indexing will be done on the 
#basis of first occurence
print(tup1.index(5))