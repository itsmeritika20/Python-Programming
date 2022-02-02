#Ques1
name = input("Enter name:")
print("Good afternoon" ,name)

#ques2
name2 = input("Enter name:")
date = input("Enter date:")
template = '''
Dear <|name|>,
you are selected
<|date|>
'''
print(template.replace("<|name|>",name2).replace("<|date|>",date))

#ques3
str = "This is  my laptop"
print(str.find("  "))
print(str.replace("  "," "))

#ques4
letter = "Dear Harry!\n\tYour python course is awesome.\nThank you"
print(letter)