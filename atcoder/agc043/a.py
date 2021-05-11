H, W = map(int, input().split())
S = [input() for _ in range(H)]

def next(h, w, pre_h, pre_w):
    if S[pre_h][pre_w] == '.' and S[h][w] == '#':
        return r[pre_h][pre_w] + 1
    else:
        return r[pre_h][pre_w]

r = []

r.append([])
r[0].append( 1 if S[0][0] == '#' else 0)
for w in range(1,W):
    r[0].append( next(0, w, 0, w-1) )

for h in range(1,H):
    r.append([])
    r[h].append( next(h, 0, h-1, 0) )

    for w in range(1, W):
        if r[h-1][w] > r[h][w-1] or \
            (r[h-1][w] == r[h][w-1] and S[h][w-1] == S[h][w]):
            r[h].append( next(h, w, h, w-1) )
        else:
            r[h].append( next(h, w, h-1, w) )

print(r[H-1][W-1])
