import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

l = range(1,N)
P = itertools.permutations(l,N-1)

ans = 0
for p in P:
    s = 0
    i = 0
    for nxt in p:
        s += T[i][nxt]
        i = nxt
    s += T[i][0]
    if s == K:
        ans += 1
print(ans)
