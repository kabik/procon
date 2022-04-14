from collections import defaultdict
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

N = II()
A = LI()

L = [0]*4
for a in A:
    L[a] += 1
dp = [[[0]*(N+3) for _ in range(N+3)] for _ in range(N+3)]

for c3 in range(N+1):
    for c2 in range(N+1 - c3):
        for c1 in range(N+1 - c3 - c2):
            sm = c1 + c2 + c3
            if sm == 0: continue

            dp[c1][c2][c3] = N/sm
            if c1 > 0: dp[c1][c2][c3] += dp[c1-1][c2][c3]   * c1 / sm
            if c2 > 0: dp[c1][c2][c3] += dp[c1+1][c2-1][c3] * c2 / sm
            if c3 > 0: dp[c1][c2][c3] += dp[c1][c2+1][c3-1] * c3 / sm

print(dp[L[1]][L[2]][L[3]])
