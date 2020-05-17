X, Y = map(int, input().split())
MOD = 10**9+7

N = 10**6+1
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


if (X+Y) % 3 != 0:
    print(0)
else:
    n = (2*X - Y) // 3
    m = (2*Y - X) // 3
    print(n, m)
    if n < 0 or m < 0:
        print(0)
    else:
        print(cmb_mod(n+m, n))
