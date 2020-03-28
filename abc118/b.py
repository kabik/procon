N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

loves = {}
for i in range(N):
    for j in range(1, A[i][0]+1):
        love = A[i][j]
        if love in loves:
            loves[love] += 1
        else:
            loves[love] = 1

print( len(list(filter( lambda x: loves[x] == N, loves ))))
