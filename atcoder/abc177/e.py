def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def prime_factorization(n):
    dct = {}
    tmp = n
    for i in range(2, int(n**0.5)+1):
        if tmp == 1:
            break
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            dct[i] = cnt
    if tmp != 1:
        dct[tmp] = 1
    if len(dct) == 0:
        dct[n] = 1
    return dct

N = int(input())
A = list(map(int, input().split()))

MAX = 10**6
exist = [False] * (MAX+1)
pairwise = True
d = {}
for a in A:
    for p in prime_factorization(a):
        if p > 1 and exist[p]:
            pairwise = False
            break
        exist[p] = True
    if not pairwise:
        break

g = A[0]
for i in range(1,N):
    g = gcd(g, A[i])
setwise = g == 1

if pairwise:
    print('pairwise coprime')
elif setwise:
    print('setwise coprime')
else:
    print('not coprime')
