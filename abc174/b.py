import sys
input = sys.stdin.readline

N, D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for xy in XY:
    x, y = xy[0], xy[1]
    if (x*x + y*y)**0.5 <= D:
        ans += 1
print(ans)
