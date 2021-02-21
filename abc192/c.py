N, K = map(int, input().split())

a = N
for _ in range(K):
    g1 = int(''.join(sorted(list(str(a)), reverse=True)))
    g2 = int(''.join(sorted(list(str(a)))))
    a = g1 - g2
print(a)
