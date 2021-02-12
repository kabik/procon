import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
XY.sort()

dp = [10**10]*N
for x,y in XY:
    i, j = x-1, y-1
    dp[j] = min(dp[j], dp[i], A[i])

ans = -10**10
for i in range(N):
    ans = max(A[i]-dp[i], ans)
print(ans)
