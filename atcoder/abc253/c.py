from collections import defaultdict
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

from queue import PriorityQueue

Q = II()

d = defaultdict(int)
minq = PriorityQueue()
maxq = PriorityQueue()
for _ in range(Q):
    q = LI()
    if q[0] == 1:
        x = q[1]
        d[x] += 1
        if d[x] == 1:
            minq.put(x)
            maxq.put(-x)
    elif q[0] == 2:
        x = q[1]
        c = q[2]
        d[x] -= min(d[x], c)
    else:
        mn = minq.get()
        while d[mn] == 0:
            mn = minq.get()
        minq.put(mn)

        mx = -maxq.get()
        while d[mx] == 0:
            mx = -maxq.get()
        maxq.put(-mx)

        print(mx-mn)
