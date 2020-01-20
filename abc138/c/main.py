n = int(input())
v = list(map(int, input().split()))

v.sort()
result = v[0]
for i in range(1, n):
    result = (result + v[i]) / 2

print(result)
