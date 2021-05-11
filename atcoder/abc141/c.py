n, k, q = map(int, input().split())

a = [-1] * q
for i in range(q):
    a[i] = int(input())

t = [0] * (n+1)
for i in range(q):
    t[ a[i] ] += 1

p = [k - q + t[i] for i in range(0, n+1)]
p[0] = 0

for i in range(1, n+1):
    if p[i] > 0:
        print('Yes')
    else:
        print('No')
