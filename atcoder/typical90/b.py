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

from itertools import product

N = II()

e = ['(',')']
P = product([0,1], repeat=N)
L = []
for pat in P:
    s = []
    for p in pat:
        s.append(e[p])
    L.append(s)

def ok(s):
    k = 0
    for c in s:
        if c == ')':
            k -= 1
        else:
            k += 1
        if k < 0:
            return False
    if k == 0:
        return True

L.sort()
for l in L:
    if ok(l):
        print(''.join(l))
