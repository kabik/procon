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

if __name__ == "__main__":
    # test primes()
    print('-- test primes() --')
    n = 100
    is_prime = primes(n)
    for i in range(n+1):
        if is_prime[i]:
            print(i)

    # test prime_factorization()
    print('-- test prime_factorization() --')
    print(36, prime_factorization(36))
    print((10**9+7)*5, prime_factorization((10**9+7)*5))
