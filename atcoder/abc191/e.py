import copy
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

to_edge   = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int, input().split())
    a,b = a-1, b-1
    to_edge[a].append((b,c))

INF = 10**12
dist_orig    = [INF]*N
visited_orig = [False]*N
def dijkstra(from_idx, edge):
    q = []
    dist = copy.copy(dist_orig)
    visited = copy.copy(visited_orig)
    for idx, d in edge[from_idx]:
        heappush(q, (d, idx))
    while q:
        prv_dist, prv_idx = heappop(q)
        if prv_idx == from_idx:
            dist[from_idx] = prv_dist
            break
        if visited[prv_idx]: continue
        visited[prv_idx] = True
        for nxt_idx, d in edge[prv_idx]:
            dist[nxt_idx] = min(dist[nxt_idx], prv_dist + d)
            heappush(q, (dist[nxt_idx], nxt_idx))
    return dist

ans = []
for i in range(N):
    dist_to   = dijkstra(i,to_edge)
    if dist_to[i] < INF:
        ans.append(dist_to[i])
    else:
        ans.append(-1)
print('\n'.join(map(str, ans)))
