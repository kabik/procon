# n以下の素数列挙
def primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if not is_prime[i]:
            continue
        k = i+i
        while k <= n:
            is_prime[k] = False
            k += i
    return is_prime

# 素因数分解
def prime_factorization(n):
    dct = {}
    tmp = n
    for i in range(2, int(n**0.5)+1):
        if tmp == 1:
            break
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            dct[i] = cnt
    if tmp != 1:
        dct[tmp] = 1
    if len(dct) == 0:
        dct[n] = 1

    return dct
