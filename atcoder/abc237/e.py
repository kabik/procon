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
    if H[u] < H[v]:
        edge[v].append( (u, H[v]-H[u]) )
        edge[u].append( (v, 2*(H[u]-H[v])) )
    else:
        edge[u].append( (v, H[u]-H[v]) )
        edge[v].append( (u, 2*(H[v]-H[u])) )

joy = [-INF]*N
joy[0] = 0
q = [(0,0)]
while q:
    from_idx, now = heappop(q)
    #debug(q=q, now=now, from_idx=from_idx)
    if now < joy[from_idx]: continue
    for to_idx, d in edge[from_idx]:
        #debug(to_idx=to_idx, d=d)
        t = now + d
        if t <= joy[to_idx]: continue
        joy[to_idx] = t
        heappush( q, (to_idx, joy[to_idx]) )

#debug(joy=joy)
print(max(joy))
