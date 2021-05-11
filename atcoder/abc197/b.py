H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = 1

for x in range(X, H):
    if S[x][Y-1] == '#': break
    ans += 1
for x in range(X-2, -1, -1):
    if S[x][Y-1] == '#': break
    ans += 1

for y in range(Y, W):
    if S[X-1][y] == '#': break
    ans += 1
for y in range(Y-2, -1, -1):
    if S[X-1][y] == '#': break
    ans += 1

print(ans)
