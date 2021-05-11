K, N = map(int, input().split())
A = list(map(int, input().split()))

mx = abs( A[0] + (K-A[N-1]) )
for i in range(N-1):
    mx = max( mx, abs(A[i]-A[i+1]) )

print(K - mx)
