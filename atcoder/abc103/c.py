N = int(input())
A = list(map(int, input().split()))

k = 0
for a in A:
    k += a-1
print(k)
