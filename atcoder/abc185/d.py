N, M = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
A.append(N+1)
A.sort()

k = 10**10
for i in range(M+1):
    d = A[i+1] - A[i] - 1
    if d > 0:
        k = min(k, d)

ans = 0
for i in range(M+1):
    d = A[i+1] - A[i] - 1
    if d % k == 0:
        ans += d // k
    else:
        ans += d // k + 1
if k == 10**10:
    print(0)
else:
    print(ans)
