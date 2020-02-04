n,k = map(int, input().split())

sum = 0
for i in range(1, n+1):
    point = i
    pro = 1/n
    while point < k:
        point *= 2
        pro /= 2
    sum += pro
print(sum)
