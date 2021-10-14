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

S = SI()
T = SI()
sn = len(S)
tn = len(T)

dp = [[0]*(tn+1) for _ in range(sn+1)]
for i in range(1,sn+1):
    for j in range(1,tn+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

k = dp[sn][tn]
ans = ['']*(k+1)
i,j = sn,tn
while k > 0:
    if S[i-1] == T[j-1]:
        ans[k]=S[i-1]
        i-=1; j-=1; k-=1
    elif dp[i][j] == dp[i-1][j]:
        i-=1
    else:
        j-=1
print(''.join(ans))
