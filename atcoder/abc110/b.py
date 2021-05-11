N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_x = max(x)
min_y = min(y)
ans = 'War'

for z in range(X+1, Y+1):
    if X < z <= Y and max_x < z <= min_y:
        ans = 'No War'
        break
print(ans)
