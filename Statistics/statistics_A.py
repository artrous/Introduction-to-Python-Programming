# Average and Standard Deviation Calculation (1st way)

import random as rn
import math

def stats1(lista):
    m = sum(lista)/len(lista)
    suma=0
    for x in lista:
        suma += (x-m)**2
    s = math.sqrt(suma/(len(lista)-1))
    return m,s

N = int(input('Numerous integers on the list: '))
L = [rn.randint(1,20)for i in range(N)]
M, sd = stats1(L)
print('List:',L)
print('Average = {:4.2f}, Standard Deviation = {:4.2f}'.format(M,sd))
