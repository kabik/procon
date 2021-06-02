import sys
sys.setrecursionlimit(1000000)

N = int(input())

X = 100000
memo = [0]*(X+1)

def f(k):
    if k == 0:
        return 0
    if memo[k]:
        return memo[k]

    res = 10**10

    # 9yen
    x = 9
    while x <= k:
        res = min(res, f(k-x) + 1)
        x *= 9

    # 6yen
    x = 6
    while x <= k:
        res = min(res, f(k-x) + 1)
        x *= 6

    # 1yen
    res = min(res, f(k-1) + 1)

    memo[k] = res
    return memo[k]

print(f(N))
