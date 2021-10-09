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
B = LI()

dp = [[0]*3001 for _ in range(N+1)]
for i in range(A[0], B[0]+1):
    dp[0][i] = 1

for i in range(1,N):
    s = [0]*3001
    s[0] = dp[i-1][0]
    for j in range(1,3001):
        s[j] = s[j-1] + dp[i-1][j]
    for j in range(A[i], B[i]+1):
        dp[i][j] = s[j] % MOD
print(sum(dp[N-1])%MOD)

'''
3
0 0 0
0 0 0
'''
