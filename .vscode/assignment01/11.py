#Write a program implement a Queue data structure.

queue = []

def enqueue():
    element = input("Enter element:")
    queue.append(element)
    print("The queue is ",element)

def dequeue():
    if not queue:
        print("The queue is empty")
    else:
        a = queue.pop(0)
        print("Removed element:",a)

def display():
    print("The queue is ",queue)

while True:
    print("Select the operation\n1.Add 2.Remove 3.Display 4.Exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid input!")