H,W = map(int, input().split())
A = [list(input()) for _ in range(H)]

for h in range(H):
    remove = True
    for w in range(W):
        if A[h][w] == '#':
            remove = False
    if remove:
        for w in range(W):
            A[h][w] = '-'

for w in range(W):
    remove = True
    for h in range(H):
        if A[h][w] == '#':
            remove = False
    if remove:
        for h in range(H):
            A[h][w] = '-'

for h in range(H):
    cnt = 0
    for w in range(W):
        if A[h][w] != '-':
            print(A[h][w], end='')
            cnt += 1
    if cnt:
        print()
