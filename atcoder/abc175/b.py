import itertools

N = int(input())
L = list(map(int, input().split()))

if N < 3:
    print(0)
else:
    patterns = list(itertools.combinations(L, 3))

    ans = 0
    for pat in patterns:
        a,b,c = pat[0], pat[1], pat[2]
        if a != b and b != c and c != a and a+b > c and b+c > a and c+a > b:
            ans += 1
    print(ans)
