# 高速素因数分解
# 複数クエリに強い
# O(NlogN)

from collections import defaultdict

def smallest_prime_factors(n):
    spf = [0]*(n+1)
    spf[1] = 1
    for i in range(2, n+1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i*i, n+1, i):
                if spf[j] == 0:
                    spf[j] = i

    return spf

def prime_factorization(n, spf):
    dct = defaultdict(int)
    x = n
    while x > 1:
        dct[spf[x]] += 1
        x //= spf[x]
    if len(dct) == 0:
        dct[n] = 1

    return dct

n = 1
spf = smallest_prime_factors(n)
print(prime_factorization(n, spf))
