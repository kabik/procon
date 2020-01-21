n = int(input())
b = list(map(int, input().split()))

sum = b[0] + b[-1]
for i in range(1, n-1):
    sum += min(b[i-1], b[i])

print(sum)
