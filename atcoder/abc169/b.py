import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
else:
    ans = 1
    for a in A:
        ans *= a
        if ans > 10**18:
            ans = -1
            break
    print(ans)
