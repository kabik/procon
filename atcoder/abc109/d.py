H,W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def next(h, w):
    if  (h == H-1 and H & 1 == 1 and w == W-1) or \
        (h == H-1 and H & 1 == 0 and w == 0):
        return -1, -1
    elif h & 1 == 0:
        if w < W-1:
            return h, w+1
        else:
            return h+1, w
    else: # h & 1 == 1
        if w > 0:
            return h, w-1
        else:
            return h+1, w

ans = []
h, w = 0,0
while h >= 0:
    nh, nw = next(h, w)
    if A[h][w] & 1 and nh >= 0:
        A[h][w] -= 1
        A[nh][nw] += 1
        ans.append(str(h+1) + ' ' + str(w+1) + ' ' + str(nh+1) + ' ' + str(nw+1))
    h, w = nh, nw
print(len(ans))
print('\n'.join(map(str, ans)))
