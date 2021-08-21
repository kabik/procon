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

def prime_factorization(n):
    dct = {}
    tmp = n
    for i in range(2, int(n**0.5)+1):
        if tmp == 1:
            break
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            dct[i] = cnt
    if tmp != 1:
        dct[tmp] = 1
    if len(dct) == 0:
        dct[n] = 1

    return dct

N,M = LI()
A = LI()

l = set()
for a in A:
    primes = prime_factorization(a)
    for p in primes:
        l.add(p)
l = sorted(list(l))
#print(l)

ans = [True] * (M+1)
ans[0] = False
ans[1] = True
for i in l:
    if i == 1: continue
    if i > M: continue
    if not ans[i]:
        continue
    ans[i] = False
    k = i+i
    while k <= M:
        ans[k] = False
        k += i

from collections import Counter
ctr = Counter(ans)
print(ctr.get(True))

for i in range(M+1):
    if ans[i]:
        print(i)
