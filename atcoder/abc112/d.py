def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)


N, M = map(int, input().split())
for d in divisors(M):
    if d * N <= M:
        ans = d
    else:
        break
print(ans)
