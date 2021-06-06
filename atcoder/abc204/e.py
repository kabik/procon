from heapq import heappop, heappush
import sys
input = sys.stdin.readline
import math

V, E = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(E)]

edge = [ [] for _ in range(V) ]
for a,b,c,d in ABCD:
    a -= 1
    b -= 1
    edge[a].append( [b,c,d] )
    edge[b].append( [a,c,d] )

INF = 10**15
dist = [INF]*V
dist[0] = 0
q = [(0,0)]
while q:
    now, from_idx = heappop(q)
    if now > dist[from_idx]: continue
    for to_idx,c,d in edge[from_idx]:
        t = max(now, round(d**0.5)-1)
        k = c + d//(t+1) + t-now
        if now+k >= dist[to_idx]: continue
        dist[to_idx] = now+k
        heappush( q, (dist[to_idx], to_idx) )

if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])
