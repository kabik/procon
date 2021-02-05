N,S,D = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 'No'
for x,y in XY:
    if x < S and y > D:
        ans = 'Yes'
print(ans)
