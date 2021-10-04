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

from itertools import permutations

N = SI()

ans = 0
pat = permutations(N)
for p in pat:
    #print(p)
    for i in range(1,len(N)):
        a = ''.join(p[:i])
        b = ''.join(p[i:])
        #print(a,b)
        if a[0] == '0' or b[0] == '0':
            continue
        else:
            ans = max(ans, int(a)*int(b))
print(ans)
