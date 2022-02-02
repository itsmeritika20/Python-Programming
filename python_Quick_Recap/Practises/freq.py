lst = [1, 1, 1, 2, 2, 3, 4, 2, 2, 5, 5, 2, 2, 5]
length = len(lst)
count = 0
uniq = []       # list to hold unique elements
dupl = []       # list to hold duplicate elements
#diplaying frequencies
i = 0
for j in lst:
    if lst.index(j) == i:
        print(j, "-", lst.count(j))
    i += 1
#displaying unique list
for i in range(0, length):
    if i in lst:
        uniq.append(i)
print(uniq)
#diplaying duplicate list
for i in lst:
    if lst.count(i) > 1:
        if i not in dupl:
            dupl.append(i)
print(dupl)
 