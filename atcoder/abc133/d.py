import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

C = [0] * N
sign = [(-1)**(i+1) for i in range(N)]

C[0] = 2*A[N-1]
for i in range(1,N):
    C[i] = 2*A[i-1] - C[i-1]

ans_n1 = C[N-1] // 2
for i in range(N-1):
    print(C[i] + sign[i] * ans_n1, end=' ')
print(ans_n1)
