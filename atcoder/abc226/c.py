import sys

sys.setrecursionlimit(10**6)
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

N = II()
T = []
K = []
A = []

for _ in range(N):
    tka = LI()
    T.append(tka[0])
    K.append(tka[1])
    if tka[1] > 0:
        A.append(tka[2:])
    else:
        A.append([])

def lis(n, l):
    for a in A[n]:
        if a-1 not in l:
            l = lis(a-1, l)
            l.add(a-1)
    return l

ans = 0
for i in lis(N-1, {N-1}):
    ans += T[i]
print(ans)

'''
4
3 0
5 1 1
7 0
2 1 2
'''
