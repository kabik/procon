import sys
from textwrap import dedent

sys.setrecursionlimit(10**6)
def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)
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
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N = II()
UV = LLI1(N-1)

edge = [[] for _ in range(N)]
for u,v in UV:
    edge[u].append(v)
    edge[v].append(u)

visited = [False]*N
LR = [[0,0] for _ in range(N)]
now = 1
def dfs(i):
    visited[i] = True
    mn, mx = INF, -INF
    for e in edge[i]:
        if not visited[e]:
            child_mn, child_mx = dfs(e)
            mn = min(mn, child_mn)
            mx = max(mx, child_mx)

    if mn == INF:
        global now
        mn, mx = now, now
        now += 1
    LR[i] = [mn, mx]
    return mn, mx
dfs(0)

for lr in LR:
    print(*lr)
