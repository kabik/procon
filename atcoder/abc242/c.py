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
#MOD = 10 ** 9 + 7
MOD = 998244353

N = II()

dp = [[0]*10 for _ in range(N)]
dp[0] = [1]*10
for i in range(1,N):
    dp[i][1] = dp[i-1][1] + dp[i-1][2]
    dp[i][9] = dp[i-1][9] + dp[i-1][8]
    for j in range(2,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    for j in range(1,10):
        dp[i][j] %= MOD
print(sum(dp[-1])%MOD)
