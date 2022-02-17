import sys

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

N,M = LI()
XY = LLI1(M)

def dfs(i):
    if path[i] > 0:
        return path[i]
    for j in edge[i]:
        #debug(i=i, j=j, d=dfs(j))
        path[i] = max(path[i], dfs(j)+1)
    return path[i]

edge = [[] for _ in range(N)]
path = [0]*N
q = []
for x, y in XY:
    edge[y].append(x)

for i in range(N):
    dfs(i)
print(max(path))
