import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))

for _ in range(Q):
    l,r = map(int, input().split())
    l,r = l-1, r-1
    used = [False]*N
    ans = 0
    XX = X[:l]+X[r+1:]
    XX.sort()
    for i in range(len(XX)):
        x = XX[i]
        mx_idx = -1
        for j in range(N):
            if used[j]: continue
            w,v = WV[j]
            if mx_idx < 0:
                if w <= x:
                    mx_idx = j
            elif w <= x and v > WV[mx_idx][1]:
                mx_idx = j
        if mx_idx >= 0:
            used[mx_idx] = True
            ans += WV[mx_idx][1]
    print(ans)
