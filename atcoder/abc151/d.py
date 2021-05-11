import queue

H,W = map(int, input().split())
S = [input() for _ in range(H)]

def nexts(h, w):
    l = []
    if h > 0   and S[h-1][w] == '.':
        l.append((h-1, w))
    if h < H-1 and S[h+1][w] == '.':
        l.append((h+1, w))
    if w > 0   and S[h][w-1] == '.':
        l.append((h, w-1))
    if w < W-1 and S[h][w+1] == '.':
        l.append((h, w+1))
    return l

def bfs(h, w):
    d = [[0]*W for _ in range(H)]
    q = queue.Queue()
    q.put((h,w))

    while not q.empty():
        v = q.get()
        vh, vw = v[0], v[1]

        for nxt in nexts(vh, vw):
            nh, nw = nxt[0], nxt[1]
            if d[nh][nw] > 0:
                continue
            d[nh][nw] = d[vh][vw] + 1
            q.put((nh, nw))
    d[h][w] = 0
    return d

ans = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue

        d = bfs(h,w)
        mx = 0
        for th in range(H):
            for tw in range(W):
                mx = max(mx, d[th][tw])
        ans = max(ans, mx)
print(ans)
