K = int(input())

g2 = [[0]*(K+1) for _ in range(K+1)]
def gcd(a, b):
    if g2[a][b] > 0:
        return g2[a][b]
    tmpa = a
    tmpb = b
    while b > 0:
        a,b = b, a%b
    g2[tmpa][tmpb] = a
    g2[tmpb][tmpa] = a
    return a

def gcd_3(a,b,c):
    g = gcd(a,b)
    g = gcd(g,c)
    return g

sm = 0
for a in range(1, K+1):
    sm += a
    for b in range(a+1, K+1):
        for c in range(b+1, K+1):
            sm += gcd_3(a,b,c) * 6
    for b in range(1, K+1):
        if a != b:
            sm += gcd(a,b) * 3

print(sm)
