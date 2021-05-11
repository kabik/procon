n = int(input())
p = list(map(int, input().split()))

min_list = []
for i in range(n):
    if i == 0:
        min_list.append(p[i])
    else:
        min_list.append( min(min_list[i-1], p[i]) )

cnt = 0
for i in range(n):
    if i == 0:
        cnt += 1
    elif min_list[i-1] >= p[i]:
        cnt += 1

print(cnt)
