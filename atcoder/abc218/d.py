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

N = II()
XY = LLI(N)
XY.sort()

d = {}
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        if y1 == y2:
            if (x1, x2) not in d:
                d[(x1,x2)] = 0
            d[(x1,x2)] += 1
#print(d)

ans = 0
for v in d.values():
    ans += v*(v-1)//2
print(ans)

'''
6
0 0
2 1
0 1
1 0
1 1
2 0
'''
