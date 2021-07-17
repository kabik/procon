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

def f(H, W, C, A):
    dp = [[INF]*W for _ in range(H)]
    x  = [[INF]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            dp[h][w] = A[h][w]
            if h > 0: dp[h][w] = min(dp[h][w], dp[h-1][w]+C)
            if w > 0: dp[h][w] = min(dp[h][w], dp[h][w-1]+C)
    for h in range(H):
        for w in range(W):
            if h > 0: x[h][w] = min(x[h][w], dp[h-1][w]+C+A[h][w])
            if w > 0: x[h][w] = min(x[h][w], dp[h][w-1]+C+A[h][w])
    ans = INF
    for h in range(H):
        for w in range(W):
            ans = min(ans, x[h][w])
    return ans

H, W, C = LI()
A = LLI(H)
B = [a[::-1] for a in A]
print( min(f(H,W,C,A), f(H,W,C,B)) )
