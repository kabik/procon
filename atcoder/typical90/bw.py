import sys
import math

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


N = int(input())

d = prime_factorization(N)
cnt = 0
for k, v in d.items():
    cnt += v

ans = math.log(cnt, 2)
ans = math.ceil(ans)
print(ans)
