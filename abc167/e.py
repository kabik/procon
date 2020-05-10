from operator import mul
from functools import reduce

N, M, K = map(int, input().split())
MOD = 998244353

def pow_mod(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow_mod(x * x % MOD, n // 2) % MOD
    else:
        return x * pow_mod(x * x % MOD, n // 2) % MOD

fact = [1]
for i in range(1,N+1):
    fact.append( (fact[i-1] * i) % MOD )

inv = [1] * (N+1)
inv[N] = pow_mod(fact[N], MOD-2)
for i in range(N, 1, -1):
    inv[i-1] = inv[i] * (i) % MOD

def cmb_mod(n,r):
    return fact[n] * inv[r] * inv[n-r] % MOD

ans = M * pow_mod(M-1, N-1) % MOD
for k in range(1, K+1):
    ans += M * pow_mod(M-1, N-1-k) * cmb_mod(N-1, k)
    ans %= MOD

print(ans)
