rate = 380000.0

n = int(input())
xu = [list(input().split()) for _ in range(n)]

ans = 0
for i in xu:
    x, u = float(i[0]), i[1]
    if u == 'BTC':
        ans += x * rate
    else:
        ans += x

print(ans)
