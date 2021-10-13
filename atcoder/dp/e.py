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

N, W = LI()
WV = LLI(N)
V_MAX = 10**5

dp = [[INF]*(V_MAX+1) for _ in range(N+1)]
for i in range(N):
    dp[i][0] = 0
for i in range(N):
    w, v = WV[i]
    for j in range(V_MAX+1):
        if j >= v:
            dp[i+1][j] = min( dp[i][j-v] + w, dp[i][j] )
        else:
            dp[i+1][j] = dp[i][j]
    tmp = dp[i]
    for k in range(20):
        if tmp[k] == INF: tmp[k] = '-'
ans = 0
for i,w in enumerate(dp[N]):
    if w <= W:
        ans = i
print(ans)
