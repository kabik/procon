N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    x1, y1 = XY[i]
    for j in range(i+1,N):
        x2, y2 = XY[j]
        ans = max(ans, ((x1-x2)**2 + (y1-y2)**2)**0.5)
print(ans)
