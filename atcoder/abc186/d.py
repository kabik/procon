N = int(input())
A = list(map(int, input().split()))
A.sort()

S = [0] * N
S[0] = A[0]
for i in range(1,N):
    S[i] = S[i-1] + A[i]

ans = 0
for i in range(N-1):
    ans += S[N-1] - S[i] - (N-1-i) * A[i]
print(ans)
