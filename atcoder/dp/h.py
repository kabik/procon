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
MOD = 10 ** 9 + 7
# MOD = 998244353

H, W = LI()
A = LLSI(H)

dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        if h < H-1 and A[h+1][w] == '.':
            dp[h+1][w] += dp[h][w]
            dp[h+1][w] %= MOD
        if w < W-1 and A[h][w+1] == '.':
            dp[h][w+1] += dp[h][w]
            dp[h][w+1] %= MOD
print(dp[H-1][W-1])
