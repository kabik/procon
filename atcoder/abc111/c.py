from collections import Counter

N = int(input())
V = list(map(int, input().split()))

ctr_0 = Counter(V[::2]).most_common()
ctr_1 = Counter(V[1::2]).most_common()

if ctr_0[0][0] != ctr_1[0][0]:
    print(N-ctr_0[0][1]-ctr_1[0][1])
else:
    if len(ctr_0) == len(ctr_1) == 1:
        print(N//2)
    else:
        a = N-ctr_0[0][1]-ctr_1[1][1]
        b = N-ctr_0[1][1]-ctr_1[0][1]
        print(min(a,b))
