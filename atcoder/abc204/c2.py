import sys

# sys.setrecursionlimit(10**6)
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
import sys
input = sys.stdin.readline

N,M = LI()
AB = LLI1(M)

V, E = N,M
edge = [ [] for _ in range(V) ]
for s,t in AB:
    edge[s].append( (1, t) )

INF = 10**15
ans = 0
for i in range(N):
    dist = [INF]*V
    dist[i] = 0
    q = [(0,i)]
    while q:
        now, from_idx = heappop(q)
        if now > dist[from_idx]: continue
        for d,to_idx in edge[from_idx]:
            t = now + d
            if t >= dist[to_idx]: continue
            dist[to_idx] = t
            heappush( q, (dist[to_idx], to_idx) )
    for j in range(N):
        if dist[j] < INF:
            ans += 1
print(ans)
