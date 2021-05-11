N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

x0, y0 = XY[0]

ans = 'No'
for i1 in range(N-2):
    for i2 in range(i1+1, N-1):
        for i3 in range(i2+1, N):
            x1, y1 = XY[i1]
            x2, y2 = XY[i2]
            x3, y3 = XY[i3]

            if x1 == x2 or x2 == x3:
                if x1 == x2 == x3:
                    ans = 'Yes'
            elif (y1 - y2) / (x1 - x2) == (y2 - y3) / (x2 - x3):
                ans = 'Yes'
print(ans)
