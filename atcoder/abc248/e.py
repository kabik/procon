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
def YN(b): print({True: 'Yes', False: 'No'}[b])
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N, K = LI()
XY = LLI(N)

eps = 10**(-9)
lines = []
used = [[False]*N for _ in range(N)]

def colinear(x1, y1, x2, y2, x3, y3):
    v1 = (y2 - y1) * (x3 - x1)
    v2 = (y3 - y1) * (x2 - x1)
    return v1 == v2

if K == 1:
    print('Infinity')
else:
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if used[i][j]: continue
            x1, y1 = XY[i]
            x2, y2 = XY[j]
            line = [i,j]
            for k in range(j+1, N):
                x3, y3 = XY[k]
                if colinear(x1, y1, x2, y2, x3, y3):
                    line.append(k)
            if len(line) >= K:
                ans += 1
                for n in range(len(line)-1):
                    for m in range(n+1, len(line)):
                        used[line[n]][line[m]] = True
    print(ans)
