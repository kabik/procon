import sys
import queue

input = sys.stdin.readline

N, Q = map(int, input().split())

node = [0] * (N+1)
nxt = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    nxt[a].append(b)
    nxt[b].append(a)

for _ in range(Q):
    p,x = map(int, input().split())
    node[p] += x

visited = [False] * (N+1)
q = queue.Queue()
q.put(1)
while not q.empty():
    v = q.get()
    visited[v] = True
    for nv in nxt[v]:
        if not visited[nv]:
            node[nv] += node[v]
            q.put(nv)

for i in range(1, N+1):
    print(node[i], end=' ')
print()
