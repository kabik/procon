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

import copy

N = II()
A = LI()

B = []
dp = [[[] for _ in range(200)] for _ in range(N+1)]
for i in range(N):
    if B: break
    for j in range(200):
        if j == 0 or dp[i][j]:
            if j == 0 and dp[i][j]:
                B = dp[i][j]
                B.append( i+1 )
                C = [i+1]
                break

            m = (j + A[i]) % 200
            if dp[i][m]:
                B = copy.copy(dp[i][j])
                B.append( i+1 )
                C = copy.copy(dp[i][m])
                break
            dp[i+1][j] = copy.copy(dp[i][j])
            dp[i+1][m] = copy.copy(dp[i][j])
            dp[i+1][m].append( i+1 )

if B:
    print('Yes')
    print(len(B), end=' ')
    for b in B: print(b, end=' ')
    print()
    print(len(C), end=' ')
    for c in C: print(c, end=' ')
    print()
else:
    print('No')
