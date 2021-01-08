S = int(input())
MOD = 10**9 + 7

if S < 3:
    print(0)
else:
    l = [0]*(S+1)
    l[0] = 1
    for i in range(3,S+1):
        l[i] = (l[i-1] + l[i-3]) % MOD
    print(l[S])
