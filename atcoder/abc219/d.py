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
X, Y = LI()
AB = LLI(N)

dp = [[[INF]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1,N+1):
    a,b = AB[i-1]
    for x in range(X+1):
        for y in range(Y+1):
            # i番目を使わない場合
            dp[i][x][y] = min(dp[i][x][y], dp[i-1][x][y])

            # i番目を使う場合
            nx = min(x+a,X)
            ny = min(y+b,Y)
            dp[i][nx][ny] = min(dp[i][nx][ny], dp[i-1][x][y]+1)
if dp[N][X][Y] == INF:
    print(-1)
else:
    print(1)
