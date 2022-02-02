
#break:used to come out of the loop
#continue:used to stop the current iteration of the loop
#pass statement: its a null statement,instructs to "do nothing"
a = [1,2, 3, 4, 5]
for item in a:
    print(item)
    if(item == 3):
        break
    print("done this iteration for",item)

print("we have finished this loop\t")

for item in a:
    print(item)
    if(item == 3):
        continue
    print("\tdone this iteration for",item)

print("\twe have finished this loop")


l = [6, 7, 8]
for item in l:
    pass