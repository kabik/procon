N,M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(M)]

A.sort()
BC.sort(key=lambda x:x[1], reverse=True)

D = [0]*N
cnt = 0
for bc in BC:
    if cnt == N: break
    b, c = bc[0], bc[1]
    for _ in range(b):
        if cnt == N: break
        D[cnt] = c
        cnt += 1

ans = 0
for i in range(N):
    ans += max(A[i], D[i])
print(ans)
