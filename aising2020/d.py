N = int(input())
X = input()
memo = [-1] * (N+1)
memo[0] = 0

def popcount(k):
    return bin(k).count('1')

def calc(k):
    pop = popcount(k)
    key = k
    if memo[key] < 0:
        k %= pop
        if k == 0:
            memo[key] = 1
        else:
            memo[key] = calc(k) + 1
    return memo[key]

K = int(X, 2)
one = popcount(K)
if one == 0:
    K_MOD = K
elif one == 1:
    K_MOD   = 0
    K_MOD_M = K
else:
    K_MOD   = K % one
    K_MOD_M = K % (one-1)
K_MOD_P = K % (one+1)

T_M = [1]*(N+1)
T_P = [1]*(N+1)
for i in range(1,N+1):
    if one > 1:
        T_M[i] = (T_M[i-1]*2) % (one-1)
    T_P[i] = (T_P[i-1]*2) % (one+1)

for i in range(N):
    if X[i] == '1':
        pop = one - 1
        k = K_MOD_M - T_M[N-i-1]
    else:
        pop = one + 1
        k = K_MOD_P + T_P[N-i-1]

    if pop == 0:
        print(0)
    else:
        k %= pop
        print(calc(k)+1)
