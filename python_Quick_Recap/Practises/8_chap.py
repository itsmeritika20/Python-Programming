#functions: a grp of statements performing a specific task
#function with arguments:a function can accept some value.
#we can put these values inside the parenthesis
def percent(marks):
    p = (marks[0] + marks[1] + marks[2])
    return p

marks1 = [12, 34, 67, 57]
percentage1 = percent(marks1)

marks2 = [22, 34, 44, 76]
percentage2 = percent(marks2)

print(percentage1, percentage2)

#default parameter value:
#we can take a value as a default argument in a function
def greet(name):
    print("Good day " + name) #function definition

greet("Ritika") #function call

