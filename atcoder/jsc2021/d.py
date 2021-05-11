N, P = map(int, input().split())
MOD = 10**9+7

def pow_mod(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_mod(x * x % MOD, n // 2) % MOD
    else:
        return x * pow_mod(x * x % MOD, n // 2) % MOD

ans = pow_mod(P-2, N-1) * (P-1) % MOD
print(ans)
