def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)

N = int(input())
A = list(map(int, input().split()))

div_0 = divisors(A[0])
div_1 = divisors(A[1])

ans = 0
for d in div_0:
    cnt = 0
    for a in A:
        if a % d == 0:
            cnt += 1
    if cnt >= N-1:
        ans = max(ans, d)
for d in div_1:
    cnt = 0
    for a in A:
        if a % d == 0:
            cnt += 1
    if cnt >= N-1:
        ans = max(ans, d)
print(ans)
