N, M, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

# -- Union Find
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

# -- Union Find


block_num = [0]*N
friend_num = [0]*N
cls_cnt = {} # cluster count

for ab in AB:
    a, b = ab[0]-1, ab[1]-1
    unite(a,b)


for ab in AB:
    a, b = ab[0]-1, ab[1]-1
    if same(a,b):
        friend_num[a] += 1
        friend_num[b] += 1


for cd in CD:
    c, d = cd[0]-1, cd[1]-1
    if same(c,d):
        block_num[c] += 1
        block_num[d] += 1


cls_cnt = {} # cluster count
for i in range(N):
    r = root(i)
    if r in cls_cnt:
        cls_cnt[r] += 1
    else:
        cls_cnt[r] = 1


for i in range(N):
    r = root(i)
    ans = cls_cnt[r] - 1 - friend_num[i] - block_num[i]
    print(ans , end=' ')
