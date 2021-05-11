def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

N, X0 = map(int, input().split())
X = list(map(int, input().split()))
X.append(X0)
X.sort()

DIFF = []
for i in range(N):
    DIFF.append(X[i+1] - X[i])

ans = DIFF[0]
for diff in DIFF:
    ans = gcd(ans, diff)
print(ans)
