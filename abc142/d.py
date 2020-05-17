A, B = map(int, input().split())

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

ap = prime_factorization(A)
bp = prime_factorization(B)
ap[1] = 1
bp[1] = 1

ans = 0
for p in ap:
    if p in bp:
        ans += 1

print(ans)
