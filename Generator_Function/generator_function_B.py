def myrange(N,logos):
    x = 1
    n = 1
    y = 1
    while n <= N:
        yield x
        n += 1
        x = pow(logos,(n-1))

    while y > N:
        yield y
        y *= 2
        
for i in myrange(5,10):
    print(i)

print()

for i in myrange(6,2):
    print(i)
