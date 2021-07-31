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
#MOD = 10 ** 9 + 7
MOD = 998244353

from heapq import heappop, heappush

N, M, K = LI()
UV = LLI1(M)
UV.sort()

broken_edge = [ [] for _ in range(N) ]
for u, v in UV:
    broken_edge[u].append( v )
    broken_edge[v].append( u )
for i in range(N):
    broken_edge[i].append( i )

dp = [[0]*N for _ in range(K+1)]
dp[0][0] = 1
for k in range(1,K+1):
    pre_sum = 0
    for i in range(N):
        pre_sum = (pre_sum + dp[k-1][i]) % MOD
    for i in range(N):
        dp[k][i] = pre_sum
        for j in broken_edge[i]:
            dp[k][i] = (dp[k][i] - dp[k-1][j]) % MOD
print(dp[K][0])
