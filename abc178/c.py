N = int(input())
MOD = 10**9 + 7

if N == 1:
    print(0)
else:
    all = 1
    for i in range(N):
        all = (all * 10) % MOD

    ex = 2
    for i in range(N):
        ex = (ex * 9) % MOD

    ov = 1
    for i in range(N):
        ov = (ov * 8) % MOD

    ans = (all - ex + ov) % MOD
    print(ans)
