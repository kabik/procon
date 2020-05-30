N = int(input())

if N % 2 == 1:
    print(0)
elif N < 2:
    print(0)
else:
    ans = 0
    d = 10
    while N // d > 0:
        ans += N // d
        d *= 5
    print(ans)
