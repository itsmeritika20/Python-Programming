#tower of hanoi in recursive way
def tower_of_hanoi(n, source, target, auxillary):
    if(n == 1):
        print("Move disk 1 from source",source,"to target",target)
        return
        
    tower_of_hanoi(n - 1, source, auxillary, target) 
    print("Move disk",n,"from source",source,"to target",target)
    tower_of_hanoi(n - 1, auxillary, target, source)

n = int(input("\nEnter number of disks:"))
tower_of_hanoi(n, 'A', 'B', 'C')