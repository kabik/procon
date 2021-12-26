def LI(): return list(map(int, input().split()))

N,A,B = LI()
P,Q,R,S = LI()

min1, max1 = max(1-A, 1-B), min(N-A, N-B)
min2, max2 = max(1-A, B-N), min(N-A, B-1)
for i in range(P, Q+1):
    for j in range(R, S+1):
        black = False
        if i-A == j-B and A + min1 <= i <= A + max1 and B + min1 <= j <= B + max1:
            black = True
        if i-A == -j+B and A + min2 <= i <= A + max2 and B - max2 <= j <= B - min2:
            black = True

        if black:
            print('#', end='')
        else:
            print('.', end='')
    print()
