from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

INF = 10**15
d = [[INF]*N for _ in range(N)]

ans = 0
for i in range(N):
    d[i][i] = 0
for a, b, c in ABC:
    d[a-1][b-1] = c
for k in range(N):
    nxt = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nxt[i][j] = min(d[i][j], d[i][k]+d[k][j])
            if nxt[i][j] < INF:
                ans += nxt[i][j]
    d = nxt
print(ans)
