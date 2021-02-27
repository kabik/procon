N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]

ans = 10**10
for a,p,x in APX:
    if x - a > 0:
        ans = min(ans, p)
if ans < 10**10:
    print(ans)
else:
    print(-1)
