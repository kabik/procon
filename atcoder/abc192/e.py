import queue
import sys
input = sys.stdin.readline

N, M, X, Y = map(int, input().split())
X,Y = X-1, Y-1
ABTK = [list(map(int, input().split())) for _ in range(M)]
E = [[] for _ in range(N)]
for a,b,t,k in ABTK:
    a, b = a-1, b-1
    E[a].append((b,t,k))
    E[b].append((a,t,k))

INF = 10**30
dist = [INF]*N
dist[X] = 0
visited = [False]*N
now = 0
q = queue.PriorityQueue()
q.put((0,X))
while q.qsize():
    _, city = q.get()
    if visited[city]:
        continue
    visited[city] = True
    now = dist[city]
    for to_idx, d, k in E[city]:
        dist[to_idx] = min(dist[to_idx], dist[city] + d + (k-now)%k)
        q.put((dist[to_idx], to_idx))
if dist[Y] < INF:
    print(dist[Y])
else:
    print(-1)
