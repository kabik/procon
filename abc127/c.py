n,m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(m)]

l_max, r_min = 1, 10**5
for di in d:
    l_max = max(l_max, di[0])
    r_min = min(r_min, di[1])

if r_min >= l_max:
    print(r_min - l_max + 1)
else:
    print(0)
