lst = [1, 1, 1, 2, 2, 3, 4, 2, 2, 5, 5, 2, 2, 5]
length = len(lst)
#diplaying frequencies
i = 0
for j in lst:
    if lst.index(j) == i:
        print(j, "-", lst.count(j))
    i += 1