# Average and Standard Deviation Calculation (2nd way)

import random as rn
import math

def stats2(lista):
    m = sum(lista)/len(lista)            
    return m, math.sqrt(sum([(x-m)**2 for x in lista])/(len(lista)-1))
    
N = int(input('Numerous integers on the list: '))
L = [rn.randint(1,20)for i in range(N)]
mo, sd = stats2(L)
print('List:',L)
print('Average = {:4.2f}, Standard Deviation = {:4.2f}'.format(*stats2(L)))
