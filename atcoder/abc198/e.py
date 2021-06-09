import sys

sys.setrecursionlimit(10**6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, sys.stdin.buffer.readline().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N = II()
C = LI()
AB = LLI1(N-1)

edge = [[] for _ in range(N)]
for a,b in AB:
    edge[a].append(b)
    edge[b].append(a)

visited = [False]*N
ok = [False]*N
def dfs(v, colors):
    if visited[v]: return
    col = C[v]

    if col not in colors or colors[col] == 0:
        ok[v] = True
        colors[col] = 1
    else:
        colors[col] += 1

    visited[v] = True
    for e in edge[v]:
        dfs(e, colors)
    colors[col] -= 1

dfs(0, {})
for i in range(N):
    if ok[i]:
        print(i+1)
