N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

ans = -1
sm = 0
for i in range(N):
    v,p = VP[i]
    sm += v * p
    if sm > X * 100:
        ans = i+1
        break
print(ans)
