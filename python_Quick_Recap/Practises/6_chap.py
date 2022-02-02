#Conditional expression:if, else, elif(elseif) conditions
#Relational operator: == , != , >= , <=
#Logical operator:true , False
'''a = 4
if(a > 4):
    print("a>4")
elif(a > 2):
    print("a>2")
else:
    print("Nothing")
'''
a = 30
if(a>4):
    print("a>4")

if(a>60):
    print("a>60")
else:
    print("nothing")

age = int(input("Enter your age:"))
if(age > 18):
    print("You can join this party")
else:
    print("you cannot join the party")

p = 45
b = 65
print(a>b)

x = True
y = False
print(x and y)
print(x or y)
print(not x)