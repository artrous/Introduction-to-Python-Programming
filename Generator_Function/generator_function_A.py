def myrange(N,logos):
    z=1
    for k in range(N):
        yield z
        z = z*logos

for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)

def myrange(N,logos):
    z=1;k=0
    while k<N:
        yield z
        z = z*logos
        k+=1
