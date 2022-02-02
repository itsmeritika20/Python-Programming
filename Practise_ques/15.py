#read file
a = str(input("Enter the name of the file with .txt extension:"))
file2 = open(a,'r')
data = file2.read()
print(data)
file2.close()