H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

def count(l, u, r, b):
    cnt = 0
    for y in range(u, b):
        for x in range(l, r):
            if S[y][x] == '1':
                cnt += 1
    return cnt


def min_op(l, u, r, b):
    mini = 10**10
    for x in range(l+1, r):
        c1 = min_op(l, u, x, b)
        c2 = min_op(x, u, r, b)
        mini = min(c1, c2, mini)

    for y in range(u, b):
        c1 = min_op(l, u, r, y)
        c2 = min_op(l, y, r, b)
        mini = min(c1, c2, mini)
