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
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

N, K = LSI()
K = int(K)

if N == '0':
    print(0)
else:
    n = list(N)
    for _ in range(K):
        x = 0
        base = 1
        for i in range(len(n)-1, -1, -1):
            x += base*int(n[i])
            base *= 8

        nxt_n = []
        while x > 0:
            if x%9 == 8:
                nxt_n.append('5')
            else:
                nxt_n.append(str(x%9))
            x //= 9
        n = list(reversed(nxt_n))
    print(''.join(n))
