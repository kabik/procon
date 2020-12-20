N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

par = [i for i in range(N+1)]
rank = [0]*(N+1)

def root(x):
    if par[x] != x:
        par[x] = root(par[x])
    return par[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x, y = root(x), root(y)
    if x == y: return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


for ab in AB:
    a, b = ab[0], ab[1]
    unite(a,b)

d = {}
for i in range(1,N+1):
    v = root(i)
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

print(max(d.values()))
