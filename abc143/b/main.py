n = int(input())
l = list(map(int, input().split()))

sum = 0
for x in range(n):
    for y in range(n):
        if x != y: sum += l[x] * l[y]

print(int(sum/2))
