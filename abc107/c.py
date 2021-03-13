import bisect

N, K = map(int, input().split())
X = list(map(int, input().split()))

i0 = bisect.bisect_left(X,0)
if i0 == 0:
    print(X[K-1])
elif i0 == N:
    print( abs(X[N-K]) )
else:
    ans = 10**20
    for i in range(K):
        if i0-i >= 0 and i0-i+K-1 < N:
            l,r = abs(X[i0-i]), X[i0-i+K-1]
            if l > r:
                ans = min(ans, l+r*2)
            else:
                ans = min(ans, l*2+r)
    print(ans)
