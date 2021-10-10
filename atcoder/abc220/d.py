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

N = II()
A = LI()

dp = [[0]*10 for _ in range(N)]
dp[0][A[0]] = 1
for i in range(N-1):
    for k in range(10):
        a = (k + A[i+1]) % 10
        b = (k * A[i+1]) % 10
        dp[i+1][a] = (dp[i+1][a] + dp[i][k]) % MOD
        dp[i+1][b] = (dp[i+1][b] + dp[i][k]) % MOD
for k in range(10):
    print(dp[N-1][k])
