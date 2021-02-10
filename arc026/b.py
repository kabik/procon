def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)

N = int(input())
divs = divisors(N)
sm = 0
for i in range( len(divs)-1 ):
    sm += divs[i]
if sm == N:
    print('Perfect')
elif sm > N:
    print('Abundant')
else:
    print('Deficient')
