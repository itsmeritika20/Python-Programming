#copy contents to another file
file = str(input("Enter the name of the file with .txt extension:"))
f1 = open(file,mode = 'r')
f2 = open(file,mode = 'w')
data = f1.readlines()
for line in data:
    f2.write(line)

f1.close()
f2.close()