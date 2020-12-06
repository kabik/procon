import sys
input = sys.stdin.readline
H,W,N,M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]
X = [[0]*W for _ in range(H)]

for cd in CD:
    c,d = cd[0]-1, cd[1]-1
    X[c][d] = -1

for ab in AB:
    a,b = ab[0]-1, ab[1]-1
    if X[a][b] == 1:
        continue
    X[a][b] = 1
    for w in range(b, -1, -1):
        if X[a][w] >= 0:
            X[a][w] = 1
        else:
            break
    for w in range(b, W):
        if X[a][w] >= 0:
            X[a][w] = 1
        else:
            break

for ab in AB:
    a,b = ab[0]-1, ab[1]-1
    if X[a][b] == 2:
        continue
    X[a][b] = 2
    for h in range(a, -1, -1):
        if X[h][b] >= 0:
            X[h][b] = 2
        else:
            break
    for h in range(a, H):
        if X[h][b] >= 0:
            X[h][b] = 2
        else:
            break

ans = 0
for h in range(H):
    for w in range(W):
        if X[h][w] > 0:
            ans += 1
print(ans)
