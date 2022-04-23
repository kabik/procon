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
