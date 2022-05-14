import sys
from xml.sax import default_parser_list

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
XY = LLI(N)
S = SI()

d = {}
for i in range(N):
    x,y = XY[i]
    c = S[i]
    if (y,c) in d:
        if c == 'R':
            d[(y,c)] = min(d[(y,c)], x)
        else:
            d[(y,c)] = max(d[(y,c)], x)
    else:
        d[(y,c)] = x


for y,c in d:
    if (y,'R') in d and (y,'L') in d and d[(y,'R')] < d[(y,'L')]:
        print('Yes')
        break
else:
    print('No')