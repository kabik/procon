H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

mn = 1000
for h in range(H):
    for w in range(W):
        mn = min(mn, A[h][w])

ans = 0
for h in range(H):
    for w in range(W):
        ans += A[h][w] - mn
print(ans)
