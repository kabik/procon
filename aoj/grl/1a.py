from heapq import heappop, heappush
import sys
input = sys.stdin.readline

V, E, r = map(int, input().split())
STD = [list(map(int, input().split())) for _ in range(E)]

edge = [ [] for _ in range(V) ]
for s,t,d in STD:
    edge[s].append( (d, t) )

INF = 10**15
dist = [INF]*V
dist[r] = 0
visited = [False]*V
visited[r] = True

q = []
for d, to_idx in edge[r]:
    dist[to_idx] = min( dist[to_idx], d )
    heappush( q, (d, to_idx) )
while q:
    _, from_idx = heappop(q)
    if visited[from_idx]: continue
    visited[from_idx] = True
    for d, to_idx in edge[from_idx]:
        dist[to_idx] = min( dist[to_idx], dist[from_idx]+d )
        heappush( q, (dist[to_idx], to_idx) )


for v in range(V):
    if dist[v] == INF:
        print('INF')
    else:
        print(dist[v])
