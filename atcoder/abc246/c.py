from operator import truediv
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

N, K, X = LI()
A = LI()

A.sort(reverse=True, key=lambda x: x%X)
#print(A)

for i,a in enumerate(A):
    if 0 < a//X < K:
        k = a//X
    elif a//X >= K:
        k = K
    else:
        k = 0
    #debug(K=K, a=a, k=k)
    A[i] -= X*k
    K -= k

for i,a in enumerate(A):
    if K == 0:
        break
    else:
        K -= 1
        A[i] = 0

print(sum(A))
