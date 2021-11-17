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

from itertools import permutations

N = II()
XY = LLI(N)

P = permutations(range(N))
sm = 0
for p in P:
    for i in range(N-1):
        x1,y1 = XY[p[i]]
        x2,y2 = XY[p[i+1]]
        sm += ((x1-x2)**2 + (y1-y2)**2)**0.5

size = 1
for i in range(1, N+1): size*=i
print(sm/size)
