N,T = map(int, input().split())
CT = [list(map(int, input().split())) for _ in range(N)]

mn = 10**10
for c,t in CT:
    if t <= T:
        mn = min(mn, c)
if mn < 10**10:
    print(mn)
else:
    print('TLE')
