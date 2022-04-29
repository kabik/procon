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

N, M, K, S, T, X = LI()
UV = LLI1(M)

S-=1
T-=1
X-=1
dp = [[[0,0] for _ in range(N)] for _ in range(K+1)]
dp[0][S][0] = 1

for i in range(K):
    for u,v in UV:
        for x in range(2):
            dp[i+1][v][x ^ (v==X)] += dp[i][u][x]
            dp[i+1][v][x ^ (v==X)] %= MOD

            dp[i+1][u][x ^ (u==X)] += dp[i][v][x]
            dp[i+1][u][x ^ (u==X)] %= MOD
print(dp[K][T][0])
