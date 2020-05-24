import sys
input = sys.stdin.readline

H, W = map(int, input().split())
S = [input() for _ in range(H)]

X = [[0]*W for _ in range(H)]
Y = [[0]*W for _ in range(H)]

for h in range(H):
    cnt = 0
    l = 0
    for w in range(W):
        if S[h][w] == '.':
            cnt += 1
        else:
            for x in range(l, w):
                X[h][x] = cnt
            l = w+1
            cnt = 0
    for x in range(l, W):
        X[h][x] = cnt

for w in range(W):
    cnt = 0
    u = 0
    for h in range(H):
        if S[h][w] == '.':
            cnt += 1
        else:
            for y in range(u, h):
                Y[y][w] = cnt
            u = h+1
            cnt = 0
    for y in range(u, H):
        Y[y][w] = cnt

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        ans = max(ans, X[h][w] + Y[h][w] - 1)
print(ans)
