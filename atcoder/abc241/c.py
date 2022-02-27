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

N = II()
S = LLSI(N)

ok = False
for h in range(N):
    for w in range(N-5):
        row_cnt = 0
        for i in range(6):
            if S[h][w+i] == '#':
                row_cnt += 1
        if row_cnt >= 4:
            ok = True
        #debug(h=h, w=w)

for h in range(N-5):
    for w in range(N):
        col_cnt = 0
        for i in range(6):
            if S[h+i][w] == '#':
                col_cnt += 1
        if col_cnt >= 4:
            ok = True
        #debug(h=h, w=w)

for h in range(N-5):
    for w in range(N-5):
        #debug(h=h, w=w)
        d1_cnt = 0
        for i in range(6):
            if S[h+i][w+i] == '#':
                d1_cnt += 1

        d2_cnt = 0
        for i in range(6):
            if S[h+5-i][w+i] == '#':
                d2_cnt += 1

        if d1_cnt >= 4 or d2_cnt >= 4:
            ok = True
YN(ok)
