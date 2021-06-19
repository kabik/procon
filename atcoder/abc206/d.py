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

import collections

N = II()
A = LI()

X=2*10**5+1
par = [i for i in range(X)]
rank = [0]*X
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

for i in range(N//2):
    unite(A[i], A[-i-1])
    unite(A[-i-1], A[i])

ans = len([i for i in range(X) if par[i] != i])
print(ans)
