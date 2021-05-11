n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(n):
    if a[i] >= b[i]:
        sum += b[i]
    elif a[i+1] < b[i] - a[i]:
        sum += a[i] + a[i+1]
        a[i+1] = 0
    else:
        sum += b[i]
        a[i+1] -= b[i] - a[i]

print(sum)
