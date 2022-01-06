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

H,W = LI()
C = LLSI(H)

wall = []
for h in range(H):
    wall.append([])
    for w in range(W):
        wall[-1].append(C[h][w]=='#')
    wall[-1].append(True)
wall.append([True]*(W+1))
# debug(wall=wall)

visited = [[False]*W for _ in range(H)]
visited[0][0] = True
q = [(0,0)]
while q:
    # debug(q=q)
    h,w = q.pop()
    # debug(wallb=wall[h+1][w])
    # debug(wallr=wall[h][w+1])
    if not wall[h+1][w] and not visited[h+1][w]:
        visited[h+1][w] = True
        q.append((h+1,w))
    if not wall[h][w+1] and not visited[h][w+1]:
        visited[h][w+1] = True
        q.append((h,w+1))

ans = 0
for h in range(H):
    # debug(visitedh=visited[h])
    for w in range(W):
        if visited[h][w]:
            ans = max(ans, h+w+1)
print(ans)
