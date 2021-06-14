import sys

#sys.setrecursionlimit(10**7)
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
A = LLSI(H)

d = [[0]*W for _ in range(H)]
for i in range(H-1, -1, -1):
    for j in range(W-1, -1, -1):
        if (i + j) % 2 == 0:
            if i == H - 1 and j == W - 1:
                d[i][j] = 0
            elif j == W - 1:
                d[i][j] = d[i + 1][j]
            elif i == H - 1:
                d[i][j] = d[i][j + 1]
            else:
                d[i][j] = max(d[i + 1][j], d[i][j + 1])
            if A[i][j] == '-':
                d[i][j] += 1
            else:
                d[i][j] -= 1
        else:
            if i == H - 1 and j == W - 1:
                d[i][j] = 0
            elif j == W - 1:
                d[i][j] = d[i + 1][j]
            elif i == H - 1:
                d[i][j] = d[i][j + 1]
            else:
                d[i][j] = min(d[i + 1][j], d[i][j + 1])
            if A[i][j] == '-':
                d[i][j] -= 1
            else:
                d[i][j] += 1

if A[0][0] == '-':
    d[0][0] -= 1
else:
    d[0][0] += 1
if d[0][0] > 0:
    print('Takahashi')
elif d[0][0] < 0:
    print('Aoki')
else:
    print('Draw')
