N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 10**10
for i in range(N):
    for j in range(N):
        if i == j:
            time = AB[i][0] + AB[j][1]
        else:
            time = max(AB[i][0], AB[j][1])
        ans = min(ans, time)
print(ans)
