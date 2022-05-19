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
A = LI()
B = LI()
C = LI()

al = [0]*46
bl = [0]*46
cl = [0]*46

for x in A:
    al[x%46] += 1
for x in B:
    bl[x%46] += 1
for x in C:
    cl[x%46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 == 0:
                ans += al[i] * bl[j] * cl[k]
print(ans)
