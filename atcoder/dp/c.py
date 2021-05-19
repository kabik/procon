N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N)]

dp = [[0,0,0] for _ in range(N)]
dp[0] = ABC[0]

for i in range(1,N):
    dp[i][0] = ABC[i][0] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = ABC[i][1] + max(dp[i-1][2], dp[i-1][0])
    dp[i][2] = ABC[i][2] + max(dp[i-1][0], dp[i-1][1])
print(max(dp[N-1]))
