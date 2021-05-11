N = int(input())
A = list(map(int, input().split()))

def gcd_step(a, b):
    return b, a % b

def gcd(a, b):
    a, b = gcd_step(a,b)
    while b > 0:
        a,b = gcd_step(a,b)

    return a

g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])

print(g)
