#remove all vowels
def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
 
string = str(input("\nEnter string:"))
rem_vowel(string)