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

a, N = LI()

dp = [INF]*(N*10+1)
q = [1]
dp[1] = 0
while q:
    x = q.pop()

    if x*a <= N*10 and dp[x]+1 < dp[x*a]:
        dp[x*a] = dp[x]+1
        #debug(x=x, xa=x*a, dpxa=dp[x*a])
        q.append(x*a)

    if x >= 10 and x%10 != 0:
        k = int(str(x)[-1]) * 10**(len(str(x))-1) + x//10
        if k <= N*10 and dp[x]+1 < dp[k]:
            dp[k] = dp[x]+1
            q.append(k)
            #debug(x=x,k=k,dpk=dp[k])

if dp[N] < INF:
    print(dp[N])
else:
    print(-1)
