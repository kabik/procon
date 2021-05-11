K = int(input())

def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def gcd_3(a,b,c):
    g = gcd(a,b)
    g = gcd(g,c)
    return g

sm = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            sm += gcd_3(a,b,c)

print(sm)
