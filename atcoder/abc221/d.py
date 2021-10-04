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

from collections import defaultdict

N = II()
AB = LLI(N)
AB.sort()

T = {0}
for a,b in AB:
    T.add(a)
    T.add(a+b)
T = sorted(list(T))
#print(T)

d = defaultdict(int)
for a,b in AB:
    d[a] += 1
    d[a+b] -= 1

for i in range(len(T)):
    t = T[i]
    if t > 0:
        #print(i, d[t], d[T[i-1]])
        d[T[i]] += d[T[i-1]]
#print(d)

ans = defaultdict(int)
keys = sorted(list(d.keys()))
#print(keys)
for i in range(len(keys)):
    #print(i,keys[i], d[keys[i]])
    if i > 0:
        ans[d[keys[i-1]]] += keys[i] - keys[i-1]
#print(ans)
for i in range(1,N+1):
    print(ans[i], end=' ')
print()

'''
4
100 10000
100 10000
200 10000
20000 40000
'''
