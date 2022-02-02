import math
print("Hello world")
print(math.floor(3.14))
print(math.floor(4.345))

##This is a comment line

a=1
b=4
c=a+b
d="This is string"
print(type(c))
print(d)

str1 = "This is our first python string"
print(str1.upper())

items = [1,2,3]
print(items)
print(type(items))

items = ["Ritika",2,3]
items[0]="Titash"
print(items)

tup1 = (1,2,3)
print(tup1)
print(type(tup1))

dict1 ={}
dict2 ={}
print(type(dict1))

dict1["virat"]=100
dict2["sachin"]=500
print(dict1)
print(dict1.get("virat"))
print(dict2.items())
print(dict2.keys())

list1 = [1,2,3,4,5]
s1 = set(list1)
print(s1)

m=5
n=10
o="Ritika"
print(str(m) + str(n) + o)
print("10-5 is",10-5)
print("10*5 is",10*5)
print("10/5 is",10/5)
print("10+5 is",10+5)

var = int(input())
print("our output is",var)
if(var>4):
    print("Variable is greater")
elif(var==2):
    print("variable is 2")
else:
    print("Variable is not greater")


for i in range(0,10):
    print(i)

i=0
while(i<10):
    print(i)
    i=i+1

def average(num1,num2):
    avg = (num1+num2)/2
    return avg
print(average(5,10))

index=3
try:
    print(index)
except Exception as e:
    print(e)


f = open("1.txt", "w")
f.write("hello world")
f.close()















