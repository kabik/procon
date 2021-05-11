N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

b = [0]*60
for a in A:
    digit = 0
    while a > 0:
        if a % 2 == 1:
            b[digit] += 1
        a = a >> 1
        digit += 1

ans = 0
for i in range(60):
    ans += 2**i * b[i] * (N-b[i])
    ans %= MOD
print(ans)
