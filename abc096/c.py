H,W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 'Yes'
for h in range(H):
    for w in range(W):
        if S[h][w] == '.': continue
        cnt = 0
        if h > 0 and S[h-1][w] == '#':
            cnt += 1
        if h < H-1 and S[h+1][w] == '#':
            cnt += 1
        if w > 0 and S[h][w-1] == '#':
            cnt += 1
        if w < W-1 and S[h][w+1] == '#':
            cnt += 1
        if cnt == 0:
            ans = 'No'
print(ans)
