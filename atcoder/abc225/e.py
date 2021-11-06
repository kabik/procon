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

from functools import cmp_to_key

def deg_cmp(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    if (x2-1)*y1 <= (x1-1)*y2:
        return -1
    else:
        return 1

N = II()
XY = LLI(N)
XY.sort(key=cmp_to_key(deg_cmp))

ans = 0
pre = (0,0)
for x,y in XY:
    px,py = pre
    if px*(y-1) >= x*py:
        ans += 1
        pre = x-1,y
print(ans)
