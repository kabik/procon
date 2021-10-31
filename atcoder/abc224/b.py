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

H,W = LI()
A = LLI(H)

ans = 'Yes'
for i1 in range(H-1):
    for i2 in range(i1, H):
        for j1 in range(W-1):
            for j2 in range(j1, W):
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    ans = 'No'
print(ans)
