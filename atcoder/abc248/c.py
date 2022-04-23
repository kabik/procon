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

N,M,K = LI()

dp = [[0]*(N*M*2) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(N*M):
        for k in range(1,M+1):
            dp[i+1][j+k] += dp[i][j]
            dp[i+1][j+k] %= MOD

print(sum(dp[N][:K+1]) % MOD)