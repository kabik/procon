import sys
sys.setrecursionlimit(500*500)

N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N-1)]

nbors = [[] for _ in range(N+1)]
for uvw in UVW:
    u,v,w = uvw[0], uvw[1], uvw[2]
    nbors[u].append((v, w))
    nbors[v].append((u, w))

dist = [-1] * (N+1)
dist[1] = 0
def dfs(now, nxt, w):
    if dist[nxt] >= 0:
        return
    dist[nxt] = dist[now] + w
    for nbor in nbors[nxt]:
        nxt2, w = nbor[0], nbor[1]
        dfs(nxt, nxt2, w)

for nbor in nbors[1]:
    nxt, w = nbor[0], nbor[1]
    dfs(1, nxt, w)

for i in range(1, N+1):
    if dist[i] % 2 == 0:
        print(0)
    else:
        print(1)
