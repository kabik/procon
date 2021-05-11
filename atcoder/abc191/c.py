H,W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W-1):
        cnt = 0
        if S[h][w]     == '#': cnt+=1
        if S[h+1][w]   == '#': cnt+=1
        if S[h][w+1]   == '#': cnt+=1
        if S[h+1][w+1] == '#': cnt+=1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
