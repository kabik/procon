import sys
input = sys.stdin.readline

N, M = map(int, input().split())
broken = [False]*N
for _ in range(M):
    a = int(input())
    broken[a] = True

MOD = 10**9+7
P = [0]*(N+2)
P[0] = 1
for i in range(N):
    if not broken[i]:
        P[i+1] = (P[i+1] + P[i]) % MOD
        P[i+2] = (P[i+2] + P[i]) % MOD
print(P[N])
