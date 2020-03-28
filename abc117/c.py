N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

if N >= M:
    print(0)
else:
    dists = [X[i+1]-X[i] for i in range(M-1)]
    if N == 1:
        print( sum(dists) )
    else:
        print( sum(sorted(dists)[:-(N-1)]) )
