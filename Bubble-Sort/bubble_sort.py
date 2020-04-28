# Bubble Sort Argorithm
# A simple solution is the following:

import random as rn

N = int(input('Lots of list items: '))
L = [rn.randint(1,100) for i in range(N)]
print('Initial list: ',L)

for i in range(N-1):                  # I am writing the range(Ν-1) that will return, AND the count Ν-2 as described by the pseudo-code
    for j in range(N-1-i):            # I am writing the range(Ν-1-i) that will return, AND the count Ν-2-i
        if L[j+1] < L[j]:             # If I want to sort in descending order I will write: if L[j+1] > L[j]:
            L[j],L[j+1]=L[j+1],L[j]   # We do not need an intermediate variable temp to replace it

print('Sorted list: ',L)
