import itertools

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

ans = 0
l = list(itertools.product([0,1], repeat=K))
for pat in l:
    dish = [False]*(N+1)
    for i in range(K):
        choice = CD[i][pat[i]]
        dish[choice] = True

    cnt = 0
    for a,b in AB:
        if dish[a] and dish[b]:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
