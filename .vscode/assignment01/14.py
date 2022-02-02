'''
Write a program to carry out the following operations on the given set
S={12,-2,56,1 ,67,3}
-number of items in set S
-maximum element in set S
-minimum element in set S
-sum of all element in set S
-obtain a new sorted set from S, set S remaining unchanged
-report whether 40 is a member of the set
-report whether 1 is an element of set S
'''
S={12,-2,56,1 ,67,3}
print(len(S))
print(max(S))
print(min(S))
print(sum(S))
print(sorted(S))
print(40 in S)
print(1 in S)