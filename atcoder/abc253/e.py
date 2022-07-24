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

N, M, K = LI()

dp = [1] * (M+1)
dp[0] = 0
for _ in range(1, N):
    acm = [0] * (M+1)
    acm[1] = dp[1]
    for i in range(2, M+1):
        acm[i] = acm[i-1] + dp[i]

    ndp = [0] * (M+1)
    for i in range(1,M+1):
        if K == 0:
            ndp[i] = acm[M]
        else:
            if i - K >= 0:
                ndp[i] += acm[i-K]
            if i + K <= M:
                ndp[i] += acm[M] - acm[i+K-1]

    for i in range(M+1):
        dp[i] = ndp[i] % MOD

print( sum(dp) % MOD )
