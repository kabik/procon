import sys
input = sys.stdin.readline

H, N = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

dp = [10**10]*(H+1)
dp[0] = 0
for i in range(H):
    for ab in AB:
        a,b = ab[0], ab[1]
        idx = i+a if i+a < H else H
        dp[idx] = min(dp[idx], dp[i]+b)
print(dp[H])
