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
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

# 桁DP
K = SI()
D = II()

klen = len(K)
dp = [[[0]*D for _ in range(2)] for _ in range(klen+1)]
dp[0][0][0] = 1
for i in range(klen):
    k = int(K[i])
    for rem in range(D):
        for dig in range(10):
            dp[i+1][1][(rem+dig)%D] = (dp[i+1][1][(rem+dig)%D] + dp[i][1][rem]) % MOD
        for dig in range(k):
            dp[i+1][1][(rem+dig)%D] = (dp[i+1][1][(rem+dig)%D] + dp[i][0][rem]) % MOD
        dp[i+1][0][(rem+k)%D] = (dp[i+1][0][(rem+k)%D] + dp[i][0][rem]) % MOD
print((dp[klen][0][0]+dp[klen][1][0]-1)%MOD)
