import itertools

N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

mn = 10**10
for pat in itertools.product([0,1], repeat=N):
    cost = 0
    skills = [0]*M
    for i in range(N):
        cost += pat[i] * CA[i][0]
        for j in range(M):
            skills[j] += pat[i] * CA[i][j+1]
    ok = True
    for j in range(M):
        if skills[j] < X:
            ok = False
    if ok:
        mn = min(mn, cost)

if mn == 10**10:
    print(-1)
else:
    print(mn)
