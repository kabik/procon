N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

def point(i, hand):
    if   T[i] == 'r' and hand == 'p':
        return P
    elif T[i] == 's' and hand == 'r':
        return R
    elif T[i] == 'p' and hand == 's':
        return S
    return 0

dp = [{'r': 0, 's': 0, 'p': 0} for _ in range(N)]

for i in range(N):
    if i - K < 0:
        dp[i]['r'] = point(i, 'r')
        dp[i]['s'] = point(i, 's')
        dp[i]['p'] = point(i, 'p')
    else:
        dp[i]['r'] = point(i, 'r') + max(dp[i-K]['s'], dp[i-K]['p'])
        dp[i]['s'] = point(i, 's') + max(dp[i-K]['r'], dp[i-K]['p'])
        dp[i]['p'] = point(i, 'p') + max(dp[i-K]['r'], dp[i-K]['s'])

ans = 0
for i in range(N - K, N):
    ans += max(dp[i]['r'], dp[i]['s'], dp[i]['p'])

print(ans)
