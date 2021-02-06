def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)

N = int(input())
div = divisors(2*N)
ans = 0
for d in div:
    if 2*N//d % 2 != d%2:
        ans += 1
print(ans)
