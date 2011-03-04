#! usr/bin/python
# Just to test

A = [1,3,5,6,7,4,3]
B = [3,5,7]
D = A
C = [0 for i in range(len(A))]
for i in range(len(A)):
    C[i]=A[i]
i=0
while i<len(A):
    for j in range(len(B)):
        if A[i]==B[j]:
            del D[i]
    i=i+1

print C
print A
