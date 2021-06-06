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
q = [(0,r)]
while q:
    now, from_idx = heappop(q)
    if now > dist[from_idx]: continue
    for d, to_idx in edge[from_idx]:
        t = now + d
        if t >= dist[to_idx]: continue
        dist[to_idx] = t
        heappush( q, (dist[to_idx], to_idx) )

for v in range(V):
    if dist[v] == INF:
        print('INF')
    else:
        print(dist[v])
