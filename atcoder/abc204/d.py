N = int(input())
T = list(map(int, input().split()))
S = sum(T)

W = S//2
dp = [[0]*(W+1) for _ in range(N+1)]
for i, t in enumerate(T):
    w,v = t,t
    for j in range(W+1):
        dp[i+1][j] = dp[i][j]
        if j-w >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-w] + v)

print(S-dp[-1][-1])
