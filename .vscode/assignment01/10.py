#Write a program to implement a Stack data structure.

stack = []

def push():
    element = input("Enter the element:")
    stack.append(element)
    print("The stack is ",stack)

def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        a = stack.pop()
        print("Removed element: ",a)
        print("Now the stack is",stack)

while True:
    print("Select the operation\n1.Push 2.Pop 3.Exit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Invalid input!")
