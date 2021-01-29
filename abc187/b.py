N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        xi, yi = XY[i]
        xj, yj = XY[j]
        if abs( (yj - yi) / (xj - xi) ) <= 1:
            ans += 1
print(ans)
