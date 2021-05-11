N = int(input())
A = list(map(int, input().split()))

sm = sum(A)
dp = [[0, -10**20]]
for i in range(N):
    dp0 = max(dp[-1][0] + A[i], dp[-1][1] - A[i])
    dp1 = max(dp[-1][0] - A[i], dp[-1][1] + A[i])
    dp.append([dp0,dp1])
print(dp[N][0])
