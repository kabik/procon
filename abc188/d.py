N, P = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(N)]

L = []
for a,b,c in ABC:
    L.append([a,-c])
    L.append([b,c])
L.sort()

ans = 0
prv_day, prv_cost = 0,0
for day, cost in L:
    cost = -cost
    if cost > 0: #a
        ans += min(P, prv_cost) * (day - prv_day - 1)
        prv_day = day-1
    else: #b
        ans += min(P, prv_cost) * (day - prv_day)
        prv_day = day
    prv_cost += cost
print(ans)
