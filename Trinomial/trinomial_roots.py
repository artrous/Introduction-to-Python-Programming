# Finding Trinomial Roots

from math import sqrt

a=float(input('Give a: '))
b=float(input('Give b: '))
c=float(input('Give c: '))

if a==0:   
    if b!=0:
        x=-c/b
        print('There is a root: ', x)
    elif c==0:
        print('Every real number is a solution!')
    else:
        print('No real number is a solution!')
else:
    D=b**2-4*a*c
    if D>0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        print('The trinomial has two real roots, the: ', x1, 'and', x2)
    elif D==0:
        x=-b/(2*a)
        print('The trinomial has a real root, the ', x)
    else:
        print('There are no real roots!')
        c1=-b/(2*a)+(sqrt(-D))*1j
        c2=-b/(2*a)-(sqrt(-D))*1j
        print('The trinomial has two complex roots, the: ', c1, 'and', c2)
        
