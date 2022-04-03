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

import math

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

T = II()
L, X, Y = LI()
Q = II()
E = [II() for _ in range(Q)]

for e in E:
    rad = 2 * math.pi * e / T
    p = (0, -math.sin(rad)*L/2, L/2-math.cos(rad)*L/2)
    b = (0, -math.sin(rad)*L/2, 0)
    t = (X, Y, 0)
    pb = distance(p, b)
    tb = distance(t, b)
    #debug(e=e, rad=rad, p=p, b=b, t=t, pb=pb, tb=tb)
    print(math.degrees(math.atan2(pb, tb)))
