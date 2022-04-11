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

N, X, Y = LI()
A = LI()

def calc(B):
    i, j, cnt_x, cnt_y, res = 0,0,0,0,0
    while i != len(B):
        while j != len(B) and (cnt_x == 0 or cnt_y == 0):
            if B[j] == X:
                cnt_x += 1
            if B[j] == Y:
                cnt_y += 1
            j += 1
        if cnt_x > 0 and cnt_y > 0:
            res += len(B) + 1 - j
        if B[i] == X:
            cnt_x -= 1
        if B[i] == Y:
            cnt_y -= 1
        i += 1
    return res

i, ans = 0,0
while i != N:
    B = []
    while i != N and Y <= A[i] <= X:
        B.append(A[i])
        i += 1
    if len(B) > 0:
        ans += calc(B)
    else:
        i += 1
print(ans)
