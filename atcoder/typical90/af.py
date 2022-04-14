import sys

# sys.setrecursionlimit(10**6)
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

import itertools

N = II()
A = LLI(N)
M = II()
XY = LLI1(M)
HATE = [[False]*N for _ in range(N)]

for x,y in XY:
    HATE[x][y] = True
    HATE[y][x] = True

ans = INF
for pat in itertools.permutations(range(N), N):
    time = 0
    ok = True
    for j, i in enumerate(pat):
        time += A[i][j]
        if j > 0 and HATE[pat[j]][pat[j-1]]:
            ok = False
    if ok:
        ans = min(ans, time)
if ans == INF:
    print(-1)
else:
    print(ans)
