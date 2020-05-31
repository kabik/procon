N = int(input())

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

if N == 1:
    print(0)
else:
    pf = prime_factorization(N)
    ans = 0
    for p in pf:
        num = pf[p]
        k = 1
        while num >= k:
            ans += 1
            num -= k
            k += 1
    print(ans)
