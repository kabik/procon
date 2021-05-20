N = int(input())
A = list(map(int, input().split()))

A.insert(0, 0)
A.append(0)

sm = 0
for i in range(N+1):
    sm += abs(A[i+1] - A[i])

for i in range(1,N+1):
    print( sm - abs(A[i+1] - A[i]) - abs(A[i] - A[i-1]) + abs(A[i+1] - A[i-1]) )
