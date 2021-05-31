N = int(input())
A = list(map(int, input().split()))

D = [0]*200
for i in range(N):
    D[A[i]%200] += 1

ans = 0
for k in range(200):
    ans += D[k] * (D[k]-1) // 2
print(ans)
