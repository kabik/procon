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

N = int(input())
M = 10**6+1
is_prime = primes(M)
P = [i for i in range(M) if is_prime[i]]

ans = 0
for i,p in enumerate(P):
    if i == 0: continue

    j = 0
    while P[j] * P[i]**3 <= N and j < i:
        j += 1

    if j > 0:
        ans += j
    else:
        break
print(ans)
