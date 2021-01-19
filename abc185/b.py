N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

now = N
last = 0
for a, b in AB:
    now -= a - last
    if now <= 0:
        break
    now = min(now + (b - a), N)
    last = b
now -= T - AB[-1][1]

if now <= 0:
    print('No')
else:
    print('Yes')
