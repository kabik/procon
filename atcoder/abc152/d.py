N = int(input())

d = {}
for i in range(1, 10):
    for j in range(1, 10):
        d[(i, j)] = 0

for i in range(1, N+1):
    s = str(i)
    head, tail = int(s[0]), int(s[-1])
    if head > 0 and tail > 0:
        d[(head, tail)] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += d[(i,j)] * d[(j,i)]
print(ans)
