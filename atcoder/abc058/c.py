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

from collections import Counter
import string

n = II()
S = LLSI(n)

d = {}
for c in string.ascii_lowercase:
    d[c] = INF
for s in S:
    ctr = Counter(s)
    for c in string.ascii_lowercase:
        if c in ctr:
            d[c] = min(d[c], ctr.get(c))
        else:
            d[c] = 0

l = []
for k,v in d.items():
    if v < INF:
        for _ in range(v):
            l.append(k)
l.sort()
print(''.join(l))
