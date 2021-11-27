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

A, B = LSI()
if len(A) > len(B):
    B = '0'*(len(A)-len(B)) + B
if len(A) < len(B):
    A = '0'*(len(B)-len(A)) + A

for i in range(1, len(A)+1):
    r = int(A[-i]) + int(B[-i])
    if r > 9:
        print('Hard')
        break
else:
    print('Easy')
