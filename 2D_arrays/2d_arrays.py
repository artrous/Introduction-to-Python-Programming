#Use a list of lists to implement two-dimensional structure square table

import random as rn
num=int(input('Give an integer: '))
L1=[[rn.randint(0,9) for i in range(num)] for k in range(num)]
for j in L1:
    print(j)

sumRow=list()
for j in range(0,len(L1[0])):
    temp=0
    for i in range(0,len(L1)):
        temp+=L1[j][i]
    sumRow.append(temp)

sumCol=list()
for j in range(0,len(L1[0])):
    temp=0
    for i in range(0,len(L1)):
        temp+=L1[i][j]
    sumCol.append(temp)

sum_diagonal=sum(L1[i][i] for i in range(num))
print('-------------')

for i in range(num):
    L1[i].append(sumRow[i])
L2=L1
for j in L2:
    print(j)
L2=sumCol
L2.append(sum_diagonal)
print(L2)
