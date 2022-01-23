from string import digits
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

import bisect

X = II()
N = len(str(X))
l = []
for i in range(100):
    l.append(i)
for d1 in range(1,10):
    for d2 in range(10):
        sub = d1-d2
        d = d2
        digits = [str(d1), str(d2)]
        for k in range(2,N):
            # d2 - d3 = sub
            # d3 = d2 - sub
            d -= sub
            if d < 0 or d > 9:
                break
            else:
                digits.append(str(d))
                l.append(int(''.join(digits)))
l.sort()
# for x in l:
#     print(x)

k = bisect.bisect_left(l, X)
print(l[k])
