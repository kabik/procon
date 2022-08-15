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

import math

N, K = LI()
A = LI()
XY = LLI(N)

have = [False]*N
for a in A:
    have[a-1] = True

mx = -INF
for i in range(N):
    if have[i]:
        continue
    mn = INF
    for j in range(N):
        if not have[j]:
            continue
        x, y = XY[i]
        x2, y2 = XY[j]
        d = (x-x2)**2 + (y-y2)**2
        mn = min(mn, d)
    mx = max(mx, mn)
print(math.sqrt(mx))
