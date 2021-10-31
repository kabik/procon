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

from itertools import combinations

N = II()
XY = LLI(N)

ans = 0
P = combinations(XY, 3)
for p in P:
    x1,y1 = p[0]
    x2,y2 = p[1]
    x3,y3 = p[2]
    if (y2-y1)*(x3-x1) != (y3-y1)*(x2-x1):
        ans += 1
print(ans)
