N, A, B = map(int, input().split())
MOD = 10**9 + 7

def pow_mod(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_mod(x * x % MOD, n // 2) % MOD
    else:
        return x * pow_mod(x * x % MOD, n // 2) % MOD

def cmb_k(k):
    X = 1
    for i in range(N-k+1, N+1):
        X = X * i % MOD

    Y = 1
    for i in range(1,k+1):
        Y = Y * i % MOD

    Y_inv = pow_mod(Y, MOD-2)
    return X * Y_inv % MOD

ans = pow_mod(2, N) - 1 - cmb_k(A) - cmb_k(B)
ans %= MOD
print(ans)
