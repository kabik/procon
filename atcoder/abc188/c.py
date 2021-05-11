import sys
N = int(input())
A = list(map(int, input().split()))

def winner(l, r):
    if l+1 == r:
        return max(A[l], A[r])
    else:
        return max(winner(l, l+(r-l)//2), winner(l+(r-l)//2+1, r))

if N == 1:
    if A[0] > A[1]:
        print(2)
    else:
        print(1)
else:
    LEN = len(A)
    mn = min( winner(0, LEN//2-1), winner(LEN//2, LEN-1))
    print(A.index(mn)+1)
