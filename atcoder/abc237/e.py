import sys

# sys.setrecursionlimit(10**6)
def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)
input = sys.stdin.buffer.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(input())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, input().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return input().rstrip()
def SI(): return input().rstrip().decode()
def LSI(): return SI().split()
def LLSI(rows_number): return [SI() for _ in range(rows_number)]
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353


from heapq import heappop, heappush

N, M = LI()
H = LI()
UV = LLI1(M)

edge = [ [] for _ in range(N) ]
for u,v in UV:
    #debug(u=u, v=v)
    edge[v].append( (max(H[u]-H[v], 0), u) )
    edge[u].append( (max(H[v]-H[u], 0), v) )

dist = [INF]*N
dist[0] = 0
q = [(0,0)]
while q:
    now, from_idx = heappop(q)
    #debug(q=q, now=now, from_idx=from_idx)
    if now > dist[from_idx]: continue
    for d, to_idx in edge[from_idx]:
        t = now + d
        #debug(to_idx=to_idx, d=d, t=t)
        if t >= dist[to_idx]: continue
        dist[to_idx] = t
        heappush( q, (dist[to_idx], to_idx) )

#debug(dist=dist)
print(max(H[0]-H[i]-dist[i] for i in range(N)))
