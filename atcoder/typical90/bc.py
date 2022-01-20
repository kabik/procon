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

N, P, Q = LI()
A = LI()

ans = 0
for i in range(N-4):
    for j in range(i+1, N-3):
        for k in range(j+1, N-2):
            for l in range(k+1, N-1):
                for m in range(l+1, N):
                    if A[i]*A[j]%P *A[k]%P *A[l]%P *A[m]%P == Q:
                        ans += 1
print(ans)
