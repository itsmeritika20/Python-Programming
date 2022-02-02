#strings, string slicing
name1 = "Adam D' Angelo"
name2 = 'Joh"n'
name3 = '''Twinkle twinkle li'l star how I wonder" what you are'''
print(name1)
print(type(name1))

print(name2)
print(type(name2))

print(name3)
print(type(name3))

#slicing:part of string
#index starts from 0 to length-1
print(name1[0])
print(name1[0:3]) #last(3) index not inclufded in output

#slicing with skip value
print(name3[1:6:2])

#string functions 
myStr = "hfihsfhladlwh"
str1 = "my name is Ritika"
print(len(myStr))
print(myStr.startswith("hfi"))
print(myStr.endswith("hfi"))
print(myStr.count('h'))
print(myStr.capitalize())
print(str1.find("name"))
print(str1.replace("name", "naam"))

#escape sequence character-comprises of more than one character but
# represents one character when used within strings
# \n(newline), \t(tab), \\"(double slash), \'(single quote)