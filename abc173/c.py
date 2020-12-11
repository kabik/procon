import itertools

def show(A):
    print('-s--')
    for a in A:
        print(a)
    print('-e--')

H,W,K = map(int, input().split())

C = [[0]*W for _ in range(H)]
for h in range(H):
    s = input()
    for w in range(W):
        if s[w] == '.':
            C[h][w] = 0
        else:
            C[h][w] = 1

ans = 0
l = [0,1]
row_pats = list(itertools.product(l, repeat=H))
col_pats = list(itertools.product(l, repeat=W))
for rp in row_pats:
    for cp in col_pats:
        R = [[0]*W for _ in range(H)]
        for h in range(H):
            if rp[h] == 1:
                for w in range(W):
                    R[h][w] = 2
        for w in range(W):
            if cp[w] == 1:
                for h in range(H):
                    R[h][w] = 2
        cnt = 0
        for h in range(H):
            for w in range(W):
                if R[h][w] < 2 and C[h][w] == 1:
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
