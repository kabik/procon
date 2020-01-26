l,r = map(int, input().split())
MOD = 2019

if r - l >= MOD:
    print(0)
else:
    min = MOD
    for i in range(l, r):
        if min == 0: break
        for j in range(i+1, r+1):
            im, jm = i % MOD, j % MOD
            val = (im * jm) % MOD
            if val < min:
                min = val
    print(min)
