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
A = LI()
B = LI()

can_a, can_b = True, True
for i in range(1, N):
    ta1, tb1, ta2, tb2 = [False]*4
    if can_a:
        ta1 = abs(A[i]-A[i-1]) <= K
        tb1 = abs(B[i]-A[i-1]) <= K
    if can_b:
        ta2 = abs(A[i]-B[i-1]) <= K
        tb2 = abs(B[i]-B[i-1]) <= K
    can_a = ta1 or ta2
    can_b = tb1 or tb2
YN(can_a or can_b)
