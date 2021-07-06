#copy
set1 = {1, 2, 3, 4} 
set2 = set1.copy() 
print(set2)

#isdisjoint
set1 = {1, 3, 5}
set2 = {2, 4, 6}
print(set1.isdisjoint(set2))

#subset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
# Returns True
print(A.issubset(B))
# Returns False
# B is not subset of A
print(B.issubset(A))

#issuperset
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
# Returns True
print(A.issuperset(B))
# Returns False
print(B.issuperset(A))
# Returns True
print(C.issuperset(B))

#update
list1 = [1, 2, 3] 
list2 = [5, 6, 7] 
# Lists converted to sets 
set1 = set(list2) 
set2 = set(list1)
# Update method 
set1.update(set2)
# Print the updated set 
print(set1) 