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

N,K = LI()
A = LI()
A.append(0)
A.sort(reverse=True)

if sum(A) <= K:
    B = [a*(a+1)//2 for a in A]
    print(sum(B))
else:
    ans = 0
    for i in range(1,N+1):
        a, na = A[i-1], A[i]
        d = (a - na)
        if K >= d*i:
            ans += i * (a*(a+1)//2 - na*(na+1)//2)
            K -= d*i
        else:
            n,m = K//i, K%i
            b, nb = a, a-n
            ans += i * (b*(b+1)//2 - nb*(nb+1)//2) + (a-n)*m
            break
    print(ans)
