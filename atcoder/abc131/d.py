N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1])

ans = 'Yes'
time = 0
for ab in AB:
    a,b = ab[0], ab[1]
    time += a
    if time > b:
        ans = 'No'

print(ans)
