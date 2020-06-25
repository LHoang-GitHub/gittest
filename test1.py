import os
import math

arr = []
for i in range(10):
    if i % 3 == 0:
        arr.append(i)
        
print(arr)
#[0, 3, 6, 9]

# top loop is the same as this list comprehension:
listOf3Mul = [x for x in range(10) if x % 3 == 0]

print(listOf3Mul)
#[0, 3, 6, 9]

'''
x = int(input())
y = int(input())
n = int(input())
ar = []
p = 0
for i in range(x + 1):
    for j in range(y + 1):
        if i + j != n:
            ar.append([])
            ar[p] = [i,j]
            p += 1
print(ar)

x = int(input())
y = int(input())
n = int(input())
print([[i,j] for i in range(x + 1) for j in range(y + 1) if ( (i + j) != n)])
'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i,j,k] for i in range(x + 1) for j in range(y+1) for k in range(z + 1) if  ( i + j + k) != n ])
