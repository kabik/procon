N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

child = [[] for _ in range(N+1)]
par = [0]*(N+1)

for ab in AB:
    a,b = ab[0], ab[1]
    child[a].append(b)
    par[b] = a

k = 0
for i in range(1,N+1):
    l = len(child[i])
    if par[i] > 0:
        l += 1
    k = max(k, l)

print(k)
col = [0] * (N+1)
col[1] = 1
for i in range(1, N):
    cnt = 0
    for c in child[i]:
        cnt += 1
        col[c] = (col[i] + cnt) % k

for ab in AB:
    b = ab[1]
    print(col[b] + 1)
