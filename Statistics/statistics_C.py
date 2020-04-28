# Average and Standard Deviation Calculation (3rd way)

import random, math

def stats3(L):    
    if N <= 1:
        return 0.0

    M, sm, sd = mean(L), 0.0, 0.0

    # Calculate Standard Deviation
    for i in L:
        sm += pow((float(i)-M), 2)
    sd = math.sqrt(sm / float(N-1))
    return sd

def mean(L):
    N, M = len(L), 0.0

    if N <= 1:
        return L[0]

    # Calculate Average
    for i in L:
        M += float(i)
    M = M / float(N)
    return M

N = int(input('Numerous integers on the list: '))
L = [random.randint(1,20) for i in range(N)]
print('List:',L)
print('Average = {:4.2f}, Standard Deviation = {:4.2f}'.format(mean(L),stats3(L)))
