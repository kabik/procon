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
XC = LLI(N)

l = [ INF]*(N+2)
r = [-INF]*(N+2)
l[0], r[0] = 0,0
l[N+1], r[N+1] = 0,0
for i in range(N):
    x, c = XC[i]
    l[c] = min(l[c], x)
    r[c] = max(r[c], x)

#print(XC)
#print(l)
##print(r)

dp = [[0, 0] for _ in range(N+2)]
pre = 0
for c in range(1, N+2):
    if l[c] == INF: continue

    if l[pre] <= r[c]:
        ll = r[c] - l[pre] + r[c] - l[c]
    else:
        ll = l[pre] - l[c]
    if r[pre] <= r[c]:
        rl = r[c] - r[pre] + r[c] - l[c]
    else:
        rl = r[pre] - l[c]
    dp[c][0] = min(dp[pre][0] + ll, dp[pre][1] + rl)

    if l[pre] >= l[c]:
        lr = l[pre] - l[c] + r[c] - l[c]
    else:
        lr = r[c] - l[pre]
    if r[pre] >= l[c]:
        rr = r[pre] - l[c] + r[c] - l[c]
    else:
        rr = r[c] - r[pre]
    dp[c][1] = min(dp[pre][0] + lr, dp[pre][1] + rr)
    pre = c
    #print(c, dp[c], ll, rl, lr, rr)
print(dp[N+1][0])
