N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

all_sm = sum(A)
sm = 0
ans = 0
for i in range(N):
    sm += A[i]
    ans += A[i] * (all_sm - sm)
    ans %= MOD
print(ans)
