N = int(input())
A = list(map(int, input().split()))

B = [A[i]-(i+1) for i in range(N)]
B.sort()

def f(B, k):
    val = 0
    for b in B:
        val += abs(b-k)
    return val

if N & 1:
    k = B[ N//2 ]
    ans = f(B, k)
else:
    k1 = B[ N//2-1 ]
    k2 = B[ N//2 ]
    ans = min( f(B, k1), f(B, k2) )
print(ans)
