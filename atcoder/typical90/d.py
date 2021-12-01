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

H, W = LI()
A = LLI(H)

SH = [0]*H
for h in range(H):
    SH[h] = 0
    for w in range(W):
        SH[h] += A[h][w]
SW = [0]*W
for w in range(W):
    SW[w] = 0
    for h in range(H):
        SW[w] += A[h][w]

for h in range(H):
    for w in range(W):
        print(SH[h] + SW[w] - A[h][w], end=' ')
    print()
