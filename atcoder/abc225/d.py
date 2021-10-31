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
MOD = 10 ** 9 + 7
# MOD = 998244353

N,Q = LI()

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

nxt = [-1]*(N+1)
pre = [-1]*(N+1)
for _ in range(Q):
    q = LI()
    #print('--' , q)
    if q[0] == 1: #1
        x,y = q[1],q[2]
        nxt[x] = y
        pre[y] = x
    elif q[0] == 2: #2
        x,y = q[1],q[2]
        nxt[x] = -1
        pre[y] = -1
    else: #3
        x = q[1]
        left, right = [], []
        i = x
        while nxt[i] >= 0:
            right.append(nxt[i])
            i = nxt[i]
        i = x
        while pre[i] >= 0:
            left.append(pre[i])
            i = pre[i]
        ans = [*left[::-1], x, *right]
        #print(left, right)
        print(len(ans), *ans)
    # print(nxt)
    # print(pre)
