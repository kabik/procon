from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

edge = [ [] for _ in range(N) ]
reachable = [[False]*N for _ in range(N)]
for i in range(N):
    reachable[i][i] = True
for a,b in AB:
    a-=1
    b-=1
    edge[a].append(b)

for i in range(N):
    q = []
    #visited = [False]*True
    for to_idx in edge[i]:
        q.append(to_idx)
    while q:
        from_idx = q.pop()
        if reachable[i][from_idx]: continue
        reachable[i][from_idx] = True
        for to_idx in edge[from_idx]:
            q.append(to_idx)

ans = 0
for i in range(N):
    for j in range(N):
        if reachable[i][j]:
            ans += 1
print(ans)
