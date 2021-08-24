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

def mult(a, b):
    return [a[0]*b[0] + a[1]*b[3],
            a[0]*b[1] + a[1]*b[4],
            a[0]*b[2] + a[1]*b[5] + a[2],
            a[3]*b[0] + a[4]*b[3],
            a[3]*b[1] + a[4]*b[4],
            a[3]*b[2] + a[4]*b[5] + a[5]]

N = II()
XY = LLI(N)

M = II()
move = [[1,0,0,0,1,0]]
for i in range(M):
    op = LI()
    if op[0] == 1:
        move.append(mult([0, 1, 0, -1, 0, 0], move[-1]))
    elif op[0] == 2:
        move.append(mult([0, -1, 0, 1, 0, 0], move[-1]))
    elif op[0] == 3:
        move.append(mult([-1, 0, op[1]*2, 0, 1, 0], move[-1]))
    else:
        move.append(mult([1, 0, 0, 0, -1, op[1]*2], move[-1]))

Q = II()
for _ in range(Q):
    a,b = LI()
    x,y = XY[b-1]
    m = move[a]
    print(m[0] * x + m[1] * y + m[2], m[3]*x + m[4] * y + m[5])
