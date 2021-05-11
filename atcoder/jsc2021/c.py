def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)

A, B = map(int, input().split())

cnt = [0]*(B+1)
for i in range(A, B+1):
    for d in divisors(i):
        cnt[d] += 1

for i in range(B, -1, -1):
    if cnt[i] >= 2:
        print(i)
        break
