par = [i for i in range(N)]
rank = [0]*N

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
