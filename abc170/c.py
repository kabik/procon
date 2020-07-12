X, N = map(int, input().split())
P = list(map(int, input().split()))
P.sort()

ans = -1
for k in range(X, -1, -1):
    if not k in P:
        ans = k
        break
for k in range(X, 102):
    if not k in P:
        if X-ans <= k-X:
            break
        else:
            ans = k
            break
print(ans)
