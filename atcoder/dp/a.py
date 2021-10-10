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

N = II()
H = LI()
H.extend([0,0])

dp = [INF]*(N+2)
dp[0] = 0
for i in range(N-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1] - H[i]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(H[i+2] - H[i]))
print(dp[N-1])
