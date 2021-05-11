N, X, Y = map(int, input().split())
cnt = [0]*N

for i in range(1, N+1):
    for j in range(i+1, N+1):
        d = min(j-i, abs(X-i) + abs(Y-j) + 1)
        cnt[d] += 1

for i in range(1,N):
    print(cnt[i])
