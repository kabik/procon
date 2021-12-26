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

N,A,B = LI()
P,Q,R,S = LI()

min1, max1 = max(1-A, 1-B), min(N-A, N-B)
min2, max2 = max(1-A, B-N), min(N-A, B-1)
for i in range(P, Q+1):
    for j in range(R, S+1):
        black = False
        if i-A == j-B and A + min1 <= i <= A + max1 and B + min1 <= j <= B + max1:
            black = True
        if i-A == -j+B and A + min2 <= i <= A + max2 and B - max2 <= j <= B - min2:
            black = True

        if black:
            print('#', end='')
        else:
            print('.', end='')
    print()
