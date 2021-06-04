N = int(input())
A = list(map(int, input().split()))

n = max(A)
r = 0
for a in A:
    if abs(n//2 - r) > abs(n//2 - a):
        r = a
print(n, r)
