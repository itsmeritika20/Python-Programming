#Create a list of cricketers. Use this list to create a dictionary in 
#which the list value become key values of the dictionary. Set the 
#values of all keys to 50 in the dictionary created.

cricketers = ["Sourav", "Sachin", "Virat", "Dhawan"]
cricketers_dictionary = dict.fromkeys(cricketers,"50")
print(cricketers_dictionary)