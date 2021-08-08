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

H, W = LI()
S = LLSI(H)

def isin(h, w):
    return 0 <= h < H and 0 <= w < W

INF = 10**15
dist = [ [INF]*W for _ in range(H)]
dist[0][0] = 0
q = [(0,0,0)]
while q:
    now, h, w = heappop(q)
    if now > dist[h][w]: continue
    for hh,ww in [ [h-1,w], [h+1,w], [h,w-1], [h,w+1]]:
        if isin(hh,ww) and S[hh][ww] == '.':
            t = now
            if t >= dist[hh][ww]: continue
            dist[hh][ww] = t
            heappush( q, (dist[hh][ww], hh, ww) )
    for hh,ww in [            [h-2,w-1], [h-2,w], [h-2,w+1],
                   [h-1,w-2], [h-1,w-1], [h-1,w], [h-1,w+1], [h-1,w+2],
                   [h,w-2],   [h,w-1],   [h,w],   [h,w+1],   [h,w+2],
                   [h+1,w-2], [h+1,w-1], [h+1,w], [h+1,w+1], [h+1,w+2],
                              [h+2,w-1], [h+2,w], [h+2,w+1]
                ]:
        if isin(hh,ww):
            t = now+1
            if t >= dist[hh][ww]: continue
            dist[hh][ww] = t
            heappush( q, (dist[hh][ww], hh, ww) )
print(dist[H-1][W-1])
