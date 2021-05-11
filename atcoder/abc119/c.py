N,A,B,C = map(int, input().split())
l = [int(input()) for _ in range(N)]

INF = 10**9

def mag(i, a, b, c):
    if i == N:
        if min(a,b,c) > 0:
            return abs(A-a) + abs(B-b) + abs(C-c) - 30
        else:
            return INF

    r0 = mag(i+1, a     , b     , c     )
    r1 = mag(i+1, a+l[i], b     , c     ) + 10
    r2 = mag(i+1, a     , b+l[i], c     ) + 10
    r3 = mag(i+1, a     , b     , c+l[i]) + 10

    return min(r0, r1, r2, r3)

print(mag(0,0,0,0))
