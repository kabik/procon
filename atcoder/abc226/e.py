import sys

# sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(input())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, input().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return input().rstrip()
def SI(): return input().rstrip().decode()
def LSI(): return SI().split()
def LLSI(rows_number): return [SI() for _ in range(rows_number)]
INF = 10 ** 16
#MOD = 10 ** 9 + 7
MOD = 998244353

N,M = LI()
UV = LLI1(M)

par = [i for i in range(N)]
rank = [0]*N
_size = [1]*N
def root(x):
    if par[x] != x:
        par[x] = root(par[x])
    return par[x]
def same(x, y):
    return root(x) == root(y)
def size(x):
    return _size[root(x)]
def unite(x, y):
    x, y = root(x), root(y)
    if x == y: return
    if rank[x] < rank[y]:
        _size[y] += _size[x]
        par[x] = y
    else:
        _size[x] += _size[y]
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

for u,v in UV:
    unite(u,v)

group = set([root(i) for i in range(N)])
vertex = [set() for _ in range(N)]
edge = [0]*N
used = [False]*N
for u,v in UV:
    used[u] = True
    used[v] = True
    r = root(u)
    vertex[r].add(u)
    vertex[r].add(v)
    edge[r] += 1

if len(set(used)) == 2:
    print(0)
else:
    ans = 1
    for g in group:
        if len(vertex[g]) == edge[g]:
            ans = (ans * 2) % MOD
        else:
            print(0)
            break
    else:
        print(ans)
