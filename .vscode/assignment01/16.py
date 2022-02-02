#Write a program to sort a dictionary in ascending / descending 
#order by value.

dict = {"one":1, "five":5,   "four":4, "two":2, "six":6, "three":3}
asc_dict = sorted(dict.items(), key=lambda x:x[1])
print(asc_dict)