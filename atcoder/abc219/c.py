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

X = SI()
N = II()
S = LLSI(N)

def cmp(a, b):
    if a == b: return 0
    m = min(len(a), len(b))
    for i in range(m):
        a_idx = X.index(a[i])
        b_idx = X.index(b[i])
        if a_idx < b_idx:
            return -1
        elif a_idx > b_idx:
            return 1
    else:
        if len(a) < len(b):
            return -1
        else:
            return 1

def cmpstr(a, b):
    return cmp(str(a), str(b))

S.sort(key=cmp_to_key(cmpstr))
print('\n'.join(S))
