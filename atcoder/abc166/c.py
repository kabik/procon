N,M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

good = [True]*N
for ab in AB:
    a, b = ab[0]-1, ab[1]-1
    if H[a] >= H[b]:
        good[b] = False
    if H[b] >= H[a]:
        good[a] = False

ans = 0
for i in range(N):
    if good[i]:
        ans += 1
print(ans)
