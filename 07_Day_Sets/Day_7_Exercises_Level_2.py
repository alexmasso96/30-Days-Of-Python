#Sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 26, 24, 25, 24]

#1. Join A and B
C = A.union(B)
print (C)

#2. Find the intersection of A and B
print(A.intersection(B))

#3. Is A a subset of B
print(A.issubset(B))

#4 Are A and B disjoint
print(A.isdisjoint(B))

#5. Join A with B and B with A
A = A.union(B)
B =B.union(A)
print(A)
print(B)

#6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7. Delete sets completely
del A
del B