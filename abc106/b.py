def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)

N = int(input())
ans = 0
for i in range(1,N+1, 2):
    if len(divisors(i)) == 8:
        ans += 1
print(ans)
