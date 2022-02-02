#for loop with else
#an optional else can be used with a for loop if the code is 
#to be executed when the loop exhausts(if we use continue)
a = [1,2,3,4,5]
for item in a:
    print(item)
    if(item == 3):
        continue
    print("done this iteration for",item)
else:
    print("We are inside else")
    print("we have finished this loop")