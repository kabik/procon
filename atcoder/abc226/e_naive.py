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

from itertools import product, repeat

N,M = LI()
UV = LLI1(M)

P = product([0,1], repeat=M)
ans = 0
for p in P:
    cnt = [0]*N
    for i in range(M):
        cnt[UV[i][p[i]]] += 1
    if set(cnt) == {1}:
        ans += 1
else:
    print(ans)
