A = list(map(float, input().split()))
Sx = A[0]
Sy = A[1]
Gx = A[2]
Gy = A[3]

ans = (Sx * Gy + Sy * Gx) / (Sy + Gy)
print(ans)
