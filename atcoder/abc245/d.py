def LI(): return list(map(int, input().split()))

N, M = LI()
A = LI()
C = LI()

B = [0] * (M+1)
B[M] = C[N+M]//A[N]
for i in range(M,-1,-1):
    B[i] = C[i+N] // A[N]
    for j in range(N+1):
        C[i+j] -= A[j] * B[i]
print(*B)
